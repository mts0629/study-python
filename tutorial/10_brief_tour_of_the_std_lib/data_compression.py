#!/usr/bin/env python

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
