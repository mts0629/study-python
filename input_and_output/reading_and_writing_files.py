#!/usr/bin/env python

# Read a text file with UTF-8 encoding
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
print(f.closed)
