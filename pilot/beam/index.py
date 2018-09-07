#!/usr/bin/env python3
import click
import time
from sys import exit
from init import initialization
from status import status_check
from start import run
from utils import check_config
from .__init__ import __version__

# Constants
CHECK_INTERVAL = 3


@click.group()
def main():
    """
    Beam Pilot - Cosmos Validator Manager
    """


@main.command('init', short_help="initialize")
@click.option('--force', default=False, is_flag=True, help="If beam directory or config file exists, overwrite it.")
def init(force):
    initialization(force)


@main.command('start', short_help="start the agent")
@click.option('--config', default="~/.beam/config.toml", help="Configuration file to use. [Default is ~/.beam/config.toml]", metavar='<FILE>')
def start(config):
    config_exists = check_config()
    if not config_exists:
        click.echo("")
        click.secho("Error: No configuration file found. (~/.beam/config.toml)", fg="red", bold=True)
        click.echo("")
        click.echo("Either create a configuration file or run `beam init`")
        click.echo("")
        exit(1)
    click.echo("")
    click.echo("Starting Beam Pilot - %s" %(time.asctime(time.localtime(time.time()))))
    click.echo("")
    while True:
        run(config)
        time.sleep(CHECK_INTERVAL)


@main.command('status', short_help="check agent status")
def status():
    status_check()


@main.command('version', short_help="check agent version")
def version():
    click.echo("")
    click.echo("Beam Pilot v%s" %(__version__))
    click.echo("")
