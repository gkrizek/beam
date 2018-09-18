import click
import os
import toml
from sys import exit
from .commands.commander import initialize
from .commands.gaiad import check_gaiad, start_gaiad, get_unbonded_steak, bond_steak
from .commands.network import get_local_ip, get_public_ip, check_connections
from .commands.voting import get_new_votes, voting_alert
from .commands.utils import get_moniker
from .logging import Log
from .http import start_server
from .utils import check_config, get_config, get_node

# Constants
CONN_WARN = 10
CONN_ERR = 20


def run(config, noupdate, firstrun, port):

    node_config = os.path.expanduser('~/.beam/node.toml')
    beam_config = os.path.expanduser('~/.beam/config.toml')
    check_config()
    configuration = get_config()
    if not os.path.exists(node_config):
        Log("No node file found. Creating one now...")
        click.echo("")
        # gather necessary information
        config_raw = open(beam_config, "r").read()
        config_file = toml.loads(config_raw)
        node_type = config_file['node_type']
        Log("Node Type: %s" %(node_type))
        local_ip = get_local_ip()
        Log("Local IP: %s" % (local_ip))
        public_ip = get_public_ip()
        Log("Public IP: %s" % (public_ip))
        moniker = get_moniker(local_ip,node_type)
        Log("Gaiad Moniker: %s" % (moniker))

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
            Log("Error writing node file: %s - %s." % (e.filename, e.strerror), Color="red", Bold=True)
            click.echo("")
            exit(1)

        click.echo("")
        Log("Node file successfully created. Continuing...")
        click.echo("")

    node_configuration = get_node()
    if firstrun and \
       configuration['gaiad']['enable'] and \
       configuration['commander']['enable']:
            os.environ['BEAM_STATUS'] = '{"message":"Good to go!","code":200}'
            start_server(port)
            Log("Getting gaiad config from Commander...")
            local_ip = node_configuration['local_ip']
            public_ip = node_configuration['public_ip']
            moniker = node_configuration['moniker']
            node_type = node_configuration['node_type']
            gaiad_dir = configuration['gaiad']['directory']
            initialize(local_ip,public_ip,moniker,node_type,gaiad_dir)
            start_gaiad()


    gaiad_running = check_gaiad()
    if gaiad_running is False and \
       configuration['gaiad']['enable']:
       # TODO: Do I need to alert that it's not running?
       # Monitor consistent failures to start
        Log("gaiad appears to be stopped. Starting gaiad...")
        start_gaiad()

    if configuration['node_type'] == 'validator':

        if configuration['validator']['bonding']:
            steak = get_unbonded_steak(configuration['validator']['address'])
            if steak > 0:
                Log("There are %s unbonded steak. Bonding now..." % (steak))
                bond_steak(steak)

        if configuration['validator']['voting']:
            votes = get_new_votes()
            if votes['new'] and configuration['alerting']:
                Log("New votes found. Alerting...")
                # TODO: Need to figure out a way to only notify of the proposal once.
                # Don't alert every time this runs.
                # Also need to find out how long until the proposal expires and do an auto-vote right before
                voting_alert()

    elif configuration['node_type'] == 'sentry':
        if configuration['sentry']['connections']:
            connections = check_connections()
            if connections > CONN_ERR and \
               configuration['sentry']['defense']:
               Log("currently have %s number of connections. Requesting help..." %(connections))
               # Tell commander about it
               os.environ['BEAM_STATUS'] = '{"message":"Large number of connections. Possible DDoS","code":515}'

            elif connections > CONN_WARN:
                Log("currently have %s number of connections. Requesting help..." %(connections))
                os.environ['BEAM_STATUS'] = '{"message":"Higher than normal connections","code":514}'


    return
