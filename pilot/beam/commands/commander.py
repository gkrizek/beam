import click
import os
from .awslambda import invoke_commander
from .gaiad import start_gaiad
from sys import exit


def announce_node(node_type):
    # TODO: determine how I need to tell people about me. If i'm a validator I need to be in private_peers. can that happen in RPC?
    return {
        "success": True,
        "message": "all good"
    }


def get_gaiad_config(node_type):
    # TODO: Need to set Moniker in config. We can either send moniker to the commander and use a jinja template, or we can just find/replace here
    config = invoke_commander({
        "action": "config_file",
        "body": {
            "type": node_type
        }
    })
    return config


def get_gaiad_nodes(node_type):
    nodes = invoke_commander({
        "action": "list",
        "body": {
            "type": node_type
        }
    })
    return nodes


def initialize(local_ip,public_ip,moniker,node_type,gaiad_dir):
    # Tell Commander about me
    report = invoke_commander({
        "action": "report",
        "body": {
            "local_ip": local_ip,
            "public_ip": public_ip,
            "moniker": moniker,
            "type": node_type
        }
    })
    click.echo(report)

    # TODO: What about the node.json and other files in ~/.gaiad/config
    gaiad_config = get_gaiad_config(node_type)
    gaiad_config_file = ("%s/config/config.toml" % (os.path.expanduser(gaiad_dir)))
    if os.path.exists(gaiad_config_file):
        os.remove(gaiad_config_file)

    # write gaiad config file
    try:
        with open(gaiad_config_file, 'w') as f:
            f.write(gaiad_config)
    except OSError as e:
        click.secho("Error writing gaiad config file: %s - %s." %(e.filename, e.strerror), fg="red", bold=True)
        click.echo("")
        exit(1)

    # Post to all nodes via RPC
    announce = announce_node(node_type)
    click.echo(announce)

    # start gaiad
    exec_gaiad = start_gaiad()
    click.echo(exec_gaiad)
    return "initialized"
