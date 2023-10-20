#!/usr/bin/env python

# Raise a specified exception: NameError
# raise NameError('HiThere')

# raise ValueError # 'raise ValueError()'

# Re-raise of the exception
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
