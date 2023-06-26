#!/usr/bin/env python

from string import Template

# Substitute placeholders in a string by Template class
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# Keyerror is thrown when placehodlers are missing
try:
    print(t.substitute(d))
except KeyError as e:
    print(f'KeyError: {e}')
# Print missing placeholders as-is
print(t.safe_substitute(d))

import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

# Change delimiter from '$' to '%' by subclass
class BatchRename(Template):
    delimiter = '%'

# Substitute file names with format string by Template
t = BatchRename('Ashley_%n%f')
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))
