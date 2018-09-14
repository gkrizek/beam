import subprocess
import click
import json
import re
from sys import exit
from .system import execute


def check_gaiad():
    gaiad_status = execute(["gaiad", "status"])
    if gaiad_status['success']:
        return True
    else:
        return False

# TODO: Need to find out how to better handle these. If this fails, what happens? How do I notify, etc.
def start_gaiad():
    start = execute(["service", "gaiad", "start"])
    return start


def stop_gaiad():
    start = execute(["service", "gaiad", "stop"])
    return start


def restart_gaiad():
    gaiad_status = execute(["gaiad", "status"])
    if gaiad_status['success']:
        stop_gaiad()
        start_gaiad()
    else:
        start_gaiad()
    return


def get_unbonded_steak(address):
    account = execute(["gaiacli", "account", address])
    info = json.loads(account['output'])
    return info['steak']['unbonded']


def bond_steak(steak, address, moniker):
    bond = execute([
        "gaiacli",
        "stake",
        "delegate",
        "--amount=%ssteak" % (steak),
        "--address-delegator=%s" % (address),
        "--address-validator=%s" % (address),
        "--from=%s"%(moniker)
    ])
    # TODO: Need to check output and make sure it actually bonds
    return bond
