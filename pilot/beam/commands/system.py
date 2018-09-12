import subprocess
import click
import re
from sys import exit


def execute(command):
    #execute commands
    return


def check_beam():
    returnprocess = False
    s = subprocess.Popen(["ps", "ax"], stdout=subprocess.PIPE)
    for x in s.stdout:
      if re.search('(.*)beam(.*)start(.*)', x):
          return True
    return False
