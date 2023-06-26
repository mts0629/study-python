#!/usr/bin/env python

import struct

# myfile.zip is compressed file of:
# file_1.txt, file_2.txt, file_3.txt, file_4.txt
with open('myfile.zip', 'rb') as f:
    data = f.read()

# Scan zip file header without zipfile module
start = 0
for i in range(3): # Show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size
