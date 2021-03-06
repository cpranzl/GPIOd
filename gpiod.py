#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Christoph Pranzl"
__copyright__ = "Copyright 2020, Christoph Pranzl"
__credits__ = ["Christoph Pranzl"]
__license__ = "GNU GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Christoph Pranzl"
__email__ = "christoph.pranzl@pranzl.net"
__status__ = "prototype"

"""
SYNOPSIS
    gpiod [-h,--help] [-v,--verbose] [--version]
DESCRIPTION
    
EXAMPLES
    
"""

import sys, os, traceback, argparse
import time
# import systemd.daemon
import random
from mpd import MPDClient
from logzero import logger
from gpiozero import Button

def main():

    # systemd.daemon.notify('READY=1')

    client = MPDClient()                # create client object
    client.timeout = 10                 # network timeout in seconds
    client.idletimeout = None           # timeout for fetching the result of the idle command
    client.connect("localhost", 6600)   # connect to host:port
    print(client.mpd_version)           # print the MPD version
    print(client.status())
    client.close()                      # send the close command
    client.disconnect()                 # disconnect from the server

    prev = Button("GPIO16")             # Prevoius
    play = Button("GPIO17")             # Play/Pause
    next = Button("GPIO18")             # Next


if __name__ == '__main__':
    parser =  argparse.ArgumentParser()
    parser.add_argument("-v", \
                        "--verbose", \
                        action="store_true", \
                        default=False, \
                        help="increase verbose output")
    parser.add_argument('--version', \
                        action='version', \
                        version='%(prog)s ' + __version__)
    args = parser.parse_args()
    main()