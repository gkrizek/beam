#!/usr/bin/env python
import argparse
from .utils import RunArgs


def beam(object):
    '''
    #parser.add_argument("initialize",help="Initialize Beam Pilot")
    #parser.add_argument("start",help="Run Beam Pilot",action="store_true")
    #parser.add_argument("status",help="Check Status of Beam Pilot",action="store_true")
    #parser.add_argument("version",help="Version of Beam Pilot",action="store_true")
    '''
    return

def main():
    parser=argparse.ArgumentParser(description="Beam Pilot - Cosmos Validator Manager")
    parser.add_argument("command",help="Beam Pilot command")
    parser.add_argument("--config",help="Configuration file to use. [Default is ~/.beam/config.toml]",dest="config")
    parser.set_defaults(func=beam)
    args=parser.parse_args()
    print(args.func(args))
