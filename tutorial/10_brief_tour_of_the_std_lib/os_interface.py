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
