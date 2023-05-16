#!/usr/bin/env python

# Read a text file with UTF-8 encoding
with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
print(f.closed)

# Read entire the file
with open('workfile', encoding="utf-8") as f:
    print(f.read())

# Read the file line by line
with open('workfile', encoding="utf-8") as f:
    print(f.readline())
    print(f.readline())

with open('workfile', encoding="utf-8") as f:
    for line in f:
        print(line, end='')

# Write to the file
with open('workfile', encoding="utf-8") as f:
    f.write('This is a test\n')

value = ('the answer', 42)
s = str(value)  # convert the tuple to string
with open('workfile', encoding="utf-8") as f:
    f.write(s)

# Change a position
with open('workfile', encoding="utf-8", 'rb+') as f:
    f.write(b'0123456789abcdef')
    f.seek(5)      # Go to the 6th byte in the file
    f.read(1)
    f.seek(-3, 2)  # Go to the 3rd byte before the end
    f.read(1)
