#!/usr/bin/env python

age: int = 1

# Don't need to initialize a variable to annotate it
a: int

child: bool
if age < 18:
    child = True
else:
    child = False

