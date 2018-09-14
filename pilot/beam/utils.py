import click
import os
import toml
from sys import exit


def config_error(message):
    click.echo("")
    click.secho(message, fg="red", bold=True)
    click.echo("")
    exit(1)
    

def check_config():
    '''
    missing additions:
    - port
    - validator-primary
    - validator-address
    - sentry-connections
    - sentry-public
    - alert_type
    '''
    beam_config = os.path.expanduser('~/.beam/config.toml')
    try:
        config_raw = open(beam_config, "r").read()
    except OSError as e:
        config_error("Error: %s - %s." % (e.filename, e.strerror))
    try:
        config = toml.loads(config_raw)
    except toml.TomlDecodeError as e:
        config_error("Error Parsing toml: \n\n%s" % (str(e)))
    try:
        node_type       = config['node_type']
        alerting        = config['alerting']
        gaiad_config    = config['gaiad']['enable']
        enable          = config['commander']['enable']
        commander       = config['commander']['commander']
        bucket          = config['commander']['bucket']

        if type(alerting) is not bool or \
            type(gaiad_config) is not bool or \
            type(enable) is not bool or \
            type(commander) is not unicode or \
            type(bucket) is not unicode:
                config['force_key_error']

    except KeyError as e:
        config_error("Error: Configuration File is invalid. Check syntax and completeness.")
        
    if node_type is 'sentry':
        try:
            suicide = config['sentry']['suicide']
            if type(suicide) is not bool:
                config['force_key_error']
        except KeyError as e:
            config_error("Error: Configuration File is invalid. Check syntax and completeness.")

    if node_type is 'validator':
        try:
            voting = config['validator']['voting']
            bonding = config['validator']['bonding']
            if type(voting) is not bool or \
                type(bonding) is not bool:
                    config['force_key_error']
        except KeyError as e:
            config_error("Error: Configuration File is invalid. Check syntax and completeness.")
    return 'Configuration is valid'


def config_exists():
    beam_config = os.path.expanduser('~/.beam/config.toml')
    if os.path.exists(beam_config):
        return True
    else:
        return False


def get_config():
    beam_config = os.path.expanduser('~/.beam/config.toml')
    if os.path.exists(beam_config):
        try:
            config_raw = open(beam_config, "r").read()
        except OSError as e:
            config_error("Error: %s - %s." % (e.filename, e.strerror))
        try:
            config = toml.loads(config_raw)
        except toml.TomlDecodeError as e:
            config_error("Error Parsing toml: \n\n%s" % (str(e)))
        return config
    else:
        return 'configuration file not found'


def get_node():
    node_config = os.path.expanduser('~/.beam/node.toml')
    if os.path.exists(node_config):
        try:
            config_raw = open(node_config, "r").read()
        except OSError as e:
            config_error("Error: %s - %s." % (e.filename, e.strerror))
        try:
            config = toml.loads(config_raw)
        except toml.TomlDecodeError as e:
            config_error("Error Parsing toml: \n\n%s" % (str(e)))
        return config
    else:
        return 'configuration file not found'
