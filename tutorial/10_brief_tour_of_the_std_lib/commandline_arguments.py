#!/usr/bin/env python

import sys

# Get a list of the commandline arguments
print(sys.argv)

import argparse

# Commandline argument parser
parser = argparse.ArgumentParser(
    prog='top',
    description='Show top lines from each file')
# Mandatory argument
parser.add_argument('filenames', nargs='+')
# Integer argument with default value, which has long/short types
parser.add_argument('-l', '--lines', type=int, default=10)

args = parser.parse_args()
print(args)
