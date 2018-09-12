import click
import os
import toml
from sys import exit
from .commands.commander import initialize
from .commands.gaiad import check_gaiad, start_gaiad, get_unbonded_steak, bond_steak
from .commands.network import get_local_ip, get_public_ip
from .commands.utils import get_moniker
from .utils import check_config, get_config


def run(config, noupdate):

    FIRST_RUN = True
    '''
    First I need to check if there is a file called `~/.beam/node.toml`. This is the beam created information file.
    If it doesn't exist, create it. It will make the necessary requests and commands to fill in all variables.
    Also, if this file doesn't exist, we need to make a Lambda call to tell Beam Commander that I just started up.
    Then continue with the run...
    If the node.toml file exists, then we skip initialization and run the checks.

    It will first make a call to Beam Commander to see if there is anything new to do.
    If there is, execute the change and reload the change.

    If it's a validator, Then check if there are unbonded steaks in account. If so bond them
    If it's a validator, check if any new votes are available. If so, alert on them.
    if the proposal is less then 2 minutes away from expring, do an auto-vote if configured to do so.
    If Sentry, Check is under DDoS attack. If so, tell Beam Commander about it.
    '''
    node_config = os.path.expanduser('~/.beam/node.toml')
    beam_config = os.path.expanduser('~/.beam/config.toml')
    check_config()
    configuration = get_config()
    if not os.path.exists(node_config):
        click.echo("No node file found. Creating one now...")
        click.echo("")
        # gather necessary information
        config_raw = open(beam_config, "r").read()
        config_file = toml.loads(config_raw)
        node_type = config_file['node_type']
        click.echo("Node Type: %s" %(node_type))
        local_ip = get_local_ip()
        click.echo("Local IP: %s" %(local_ip))
        public_ip = get_public_ip()
        click.echo("Public IP: %s" %(public_ip))
        moniker = get_moniker(local_ip,node_type)
        click.echo("Gaiad Moniker: %s" %(moniker))

        data = {}
        data['node_type'] = node_type
        data['local_ip'] = local_ip
        data['public_ip'] = public_ip
        data['moniker'] = moniker
        # write node config file
        try:
            formatted_data = toml.dumps(data).rstrip()
            with open(node_config, 'w') as f:
                f.write(formatted_data)
        except OSError as e:
            click.secho("Error writing node file: %s - %s." % (e.filename, e.strerror), fg="red", bold=True)
            click.echo("")
            exit(1)

        click.echo("")
        click.echo("Node file successfully created. Continuing...")
        click.echo("")

    if configuration['gaiad']['enable'] and \
       configuration['commander']['enable'] and \
       FIRST_RUN:
        click.echo("Checking into commander....")
        initialize(local_ip,public_ip,moniker,node_type)
        start_gaiad()

        FIRST_RUN = False


    click.echo("Now running checks...")
    check_gaiad()
    if configuration['node_type'] is 'validator':
        steak = get_unbonded_steak()
        if steak > 0:
            click.echo("There are %s unbonded steak. Bonding now..." %(steak))
            bond_steak(steak)
    else if configuration['node_type'] is 'sentry':

        print("sentry")

    return
