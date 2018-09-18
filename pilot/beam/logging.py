import click
import datetime
import time


def Log(message, Color='white', Bold=False):
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    click.secho("%s - %s" % (timestamp, message), fg=Color, bold=Bold)
    return