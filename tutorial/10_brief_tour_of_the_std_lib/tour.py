#!/usr/bin/env python

import os

# Get current working directory
wd = os.getcwd()
print(wd)

# Change directory
os.chdir('/bin')
# Run command
os.system('ls | grep system')

# Get a list of the names in the module namespace
print(dir(os))

# Show the help for an interactive mode
# help(os)

os.chdir(wd)

import shutil

# Copy, move, remove files
shutil.copyfile('../README.md', './README.md')
shutil.move('./README.md', './copy.md')
os.remove('./copy.md')

import glob

# Get a list of path names by wildcard
print(glob.glob('./*/*.py'))

import sys

# Get a list of the commandline arguments
print(sys.argv)

# Redirect a message to stderr
sys.stderr.write('Warning, log file not found starting a new one\n')

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

import re

# Find patterns by regex
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
# Substitute patterns by regex
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
# Substitute patterns by string method
print('tea for too'.replace('too', 'two'))

import math

# cos(PI/4)
print(math.cos(math.pi / 4))
# log_2(1024)
print(math.log(1024, 2))

import random

# Random choice
for _ in range(3):
    print(random.choice(['apple', 'pear', 'banana']))

# Random sampling from a sequence
print(random.sample(range(100), 10))

# Get random float in [0, 1)
for _ in range(3):
    print(random.random())

# Get random integer chosen from the range
for _ in range(3):
    print(random.randrange(6))

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

# Mean, median, variance of the iterable object
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))

from urllib.request import urlopen

# Get UTC from 'worldtimeapi.org'
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()
        if line.startswith('datetime'):
            print(line.rstrip())

# Send e-mail with SMTP
# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
# 
# Beware the Ides of March.
# """)
# server.quit()

from datetime import date

# Construct and print formatted date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# Calendar arithmetic for dates
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)

import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

# Compress binary data
t = zlib.compress(s)
print(len(t))
# Decompress the data
print(zlib.decompress(t))
# Calculate checksum (by Adler-32 algorithm)
print(zlib.crc32(s))

from timeit import Timer

# Compare elapsed time of swapping variables by ...
# Using temoporal variable
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# Using unpacking of a tuple
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

import doctest

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

# Automatically validate the embedded tests in docstrings
doctest.testmod()
