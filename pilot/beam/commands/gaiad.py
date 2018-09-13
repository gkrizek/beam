import subprocess
import click
import re
from sys import exit
from .system import execute


def check_gaiad():
    # TODO: Maybe convert this to gaiad status and check it's return code
    s = subprocess.Popen(["ps", "ax"],stdout=subprocess.PIPE)
    for x in s.stdout:
      if re.search('(.*)gaiad(.*)start(.*)', x):
          return True
    return False
    

def restart_gaiad():
    # restart gaiad
    return


def start_gaiad():
    print('starting gaiad...')
    return


def get_unbonded_steak():

    return 0


def bond_steak(steak):

    return
