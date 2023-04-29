#!/usr/bin/env python

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)

# del statement: remove items from the list
del a[0] # By index
print(a)

del a[2:4] # By slicing
print(a)

del a[:]
print(a)

del a # Delete entire variables
# print(a) # NameError until an another value is assigned to 'a'
