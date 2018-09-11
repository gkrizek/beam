import click
import os
import toml
from sys import exit


def config_error(message):
    click.echo("")
    click.secho(message, fg="red", bold=True)
    click.echo("")
    exit(1)


def is_boolen(key,value):
    if type(value) is bool:
        return
    else:
        config_error("Configuration Error: Expecting %s to be a boolen" %(key))


def is_string(key,value):
    if type(value) is str:
        return
    else:
        config_error("Configuration Error: Expecting %s to be a string" %(key))



def check_config():
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
        config['node_type']
        config['alerting']
        config['gaiad_config']
        config['commander']['enabled']
        config['commander']['commander']
        config['commander']['bucket']
        config['node_type']
    except KeyError as e:
        config_error("Error: Configuration File is invalid. Check syntax and completeness.")
    return


def config_exists():
    beam_config = os.path.expanduser('~/.beam/config.toml')
    if os.path.exists(beam_config):
        return True
    else:
        return False