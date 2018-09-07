#!/usr/bin/env python3
import click


@click.group()
def main():
    """
    Beam Pilot
    """

@main.command('init', short_help="Initialize Beam Pilot")
@main.command('start', short_help="Run Beam Pilot")
@main.command('status', short_help="Check status of Beam Pilot")
@main.command('version', short_help="Check version of Beam Pilot")
@click.option('--config', help="Configuration file to use. [Default is ~/.beam/config.toml]")

def init(config):
    print(config)
    click.echo('init command')


def start(config):
    print(config)
    click.echo('start command')


def status(config):
    print(config)
    click.echo('status command')


def version(config):
    print(config)
    click.echo('version command')
