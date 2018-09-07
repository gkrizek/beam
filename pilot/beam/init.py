import click
import os
import sys
from shutil import rmtree, copy
from sys import exit


def remove_configs(beam_directory, beam_config):
    for f in [beam_directory, beam_config]:
        if os.path.exists(f):
            try:
                rmtree(f)
            except OSError as e:
                click.secho("Error: %s - %s." % (e.filename, e.strerror), fg="red", bold=True)
                click.echo("")
                exit(1)
    return


def failure():
    click.echo("")
    click.secho("Initialization Failed:", fg="red", bold=True)
    click.echo("")
    click.echo("Either the '~/.beam' directory or the '~/.beam/config.toml' file already exist.")
    click.echo("Remove them or re-run with '--force' to overwrite them.")
    click.echo("")
    exit(1)


def initialization(force):
    beam_directory = os.path.expanduser('~/.beam')
    beam_config = os.path.expanduser('~/.beam/config.toml')

    if not os.path.isdir(beam_directory) and \
        not os.path.exists(beam_config) or \
        force is True:
            click.echo("")

            if force is True:
                remove_configs(beam_directory, beam_config)

            '''
            Should we add a flag or something that support a "remote" source when initializing?
            Maybe even have a command like `beam init validator` or `beam init sentry`.
            I'm concerned with bootstrapping capabilities. This command currently doesn't really help much
            with that and in a truly automated setup this would require a seperate software/service to manage
            the configs. But maybe that's what we want and this only to be used "when developing".
            '''

            try:
                current_path = os.path.abspath(__file__)
                current_dir = os.path.dirname(current_path)
                os.mkdir(beam_directory)
                copy(os.path.abspath(os.path.join(current_dir,'../configs/example-config.toml')), beam_config)
            except OSError as e:
                click.secho("Error writing configs: %s - %s." % (e.filename, e.strerror), fg="red", bold=True)
                click.echo("")
                exit(1)

            click.echo("Configuration file successfully written.")
            click.echo("")

    else:
        failure()
