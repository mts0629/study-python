#!/usr/bin/env python

# An example of standard module: sys
import sys

# Primary prompt
# sys.ps1
# Secondary prompt
# sys.ps2
# Only on an interactive mode

# Module search path
print(sys.path)

# Append new search path
sys.path.append('/uft/guido/lib/python')
print(sys.path)

# Native byte order
print(sys.byteorder)

# Dictionary that maps module names to modules which have already been loaded
print(sys.modules)

# etc.
