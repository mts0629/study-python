#!/usr/bin/env python

# Read a text file with UTF-8 encoding
with open('read.txt', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
print(f.closed)

# Read entire the file
with open('read.txt', encoding="utf-8") as f:
    print(f.read())

# Read the file line by line
with open('read.txt', encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())

with open('read.txt', encoding="utf-8") as f:
    for line in f:
        print(line, end='')

# Write to the file
with open('write.txt', 'w', encoding="utf-8") as f:
    f.write('This is a test\n')

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
with open('write2.txt', 'w', encoding="utf-8") as f:
    f.write(s)

# Change a position
with open('write.bin', 'wb+') as f:
    f.write(b'0123456789abcdef')
    f.seek(5)      # Go to the 6th byte in the file
    print(f.read(1))
    f.seek(-3, 2)  # Go to the 3rd byte before the end
    print(f.read(1))

import json

x = [1, 'simple', 'list']

# Serialize an object to a JSON formatted string
print(f"{json.dumps(x)}, {type(json.dumps(x))}")

with open('out.json', 'w', encoding='utf-8') as f:
    # Serialize the object as a JSON formatted stream
    json.dump(x, f, indent=4)

with open('out.json', 'r', encoding='utf-8') as f:
    # Deserialize the JSON file object to a Python object
    x = json.load(f)
    print(f"{x}, {type(x)}")
