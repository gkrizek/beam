import subprocess
import click
from .commands.system import check_beam


def running():
    click.echo("")
    click.echo("Beam Pilot is running")
    click.echo("")
    return


def stopped():
    click.echo("")
    click.echo("Beam Pilot is stopped")
    click.echo("")
    return


def error():
    click.echo("")
    click.secho("Error retrieving Beam Pilot status", fg="red", bold=True)
    click.echo("")
    exit(1)


def status_check():
    try:
        beam_running = check_beam()
        if beam_running:
            running()
        else:
            stopped()
    except Exception as e:
        print(e)
        error()
    return
