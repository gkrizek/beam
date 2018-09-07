import subprocess
import click
import re
from sys import exit


def running():
    click.echo("")
    click.echo("Beam Pilot is running")
    click.echo("")
    return


def stopped():
    click.echo("")
    click.echo("Beam Pilot is not running")
    click.echo("")
    return


def error():
    click.echo("")
    click.secho("Error retrieving Beam Pilot status", fg="red", bold=True)
    click.echo("")
    exit(1)


def status_check():
    returnprocess = False
    try:
        s = subprocess.Popen(["ps", "ax"],stdout=subprocess.PIPE)
    except Exception:
        error()
    for x in s.stdout:
      if re.search('(.*)beam(.*)start(.*)', x):
          returnprocess = True
    if returnprocess == False:
      stopped()
    if returnprocess == True:
      running()
    return
