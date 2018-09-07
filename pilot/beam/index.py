#!/usr/bin/env python3
import click
from init import initialization
from .__init__ import __version__


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
    print(config)
    click.echo('start command')


@main.command('status', short_help="check agent status")
def status():
    click.echo('status command')


@main.command('version', short_help="check agent version")
def version():
    click.echo("")
    click.echo("Beam Pilot v%s" %(__version__))
    click.echo("")
