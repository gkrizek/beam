#!/usr/bin/env python3
import click


@click.group()
def main():
    """
    Beam Pilot - Cosmos Validator Manager
    """


@main.command('init', short_help="initialize")
def init():
    click.echo('init command')


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
    click.echo('version command')
