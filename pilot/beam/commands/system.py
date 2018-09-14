import subprocess
import click
import re
from sys import exit


def execute(command):
    # Commands need to be sent in a Popen compatible way. Ex: ["ps", "aux"]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.returncode is 0:
        return {
            "success": True,
            "code": process.returncode,
            "output": process.stdout.read()
        }
    else:
        return {
            "success": False,
            "code": process.returncode,
            "output": process.stdout.read()
        }


def check_beam():
    s = subprocess.Popen(["ps", "ax"], stdout=subprocess.PIPE)
    for x in s.stdout:
      if re.search('(.*)beam(.*)start(.*)', x):
          return True
    return False
