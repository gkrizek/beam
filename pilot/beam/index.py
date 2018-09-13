#!/usr/bin/env python3
import click
import time
import os
from sys import exit
from .init import initialization
from .reset import reset_beam
from .status import status_check
from .start import run
from .utils import config_exists
from .__init__ import __version__

# Constants
CHECK_INTERVAL = 3


@click.group()
def beam():
    """
    \b
     _ )  __|    \     \  | 
     _ \  _|    _ \   |\/ | 
    ___/ ___| _/  _\ _|  _| 


    Beam Pilot - Cosmos Infrastructure Manager
    """


@beam.command('init', short_help="initialize")
@click.option('--force', default=False, is_flag=True, help="if beam directory or config file exists, overwrite it.")
def init(force):
    initialization(force)


@beam.command('start', short_help="start the agent")
@click.option('--config', default="~/.beam/config.toml", help="configuration file to use. [default is ~/.beam/config.toml]", metavar='<FILE>')
@click.option('--noupdate', default=False, is_flag=True, help="disable gaiad configuration file update from commander.")
@click.option('--port', default=9393, help="port to listen on", metavar='<PORT>')
def start(config, noupdate, port):
    exists = config_exists()
    if not exists:
        click.echo("")
        click.secho("Error: No configuration file found. (~/.beam/config.toml)", fg="red", bold=True)
        click.echo("")
        click.echo("Either create a configuration file or run `beam init`")
        click.echo("")
        exit(1)
    click.echo("")
    click.echo("Starting Beam Pilot - %s" %(time.asctime(time.localtime(time.time()))))
    click.echo("")
    
    from .commands.system import execute
    test = execute(["ps", "ax"])
    print(test)

    firstrun = True
    while True:
        run(config, noupdate, firstrun, port)
        time.sleep(CHECK_INTERVAL)
        firstrun = False


@beam.command('status', short_help="check agent status")
def status():
    status_check()


@beam.command('reset', short_help="reset the Beam Pilot node")
def reset():
    reset_beam()
    click.echo("")
    click.echo("Node reset")
    click.echo("")


@beam.command('version', short_help="check agent version")
def version():
    click.echo("")
    click.echo("Beam Pilot v%s" %(__version__))
    click.echo("")
