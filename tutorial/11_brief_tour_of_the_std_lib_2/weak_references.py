#!/usr/bin/env python

import weakref, gc

class A:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

# Create a reference
a = A(10)
# Weak reference: reference which is not captured by garbage collector
d = weakref.WeakValueDictionary()
d['primary'] = a    # Does not create a reference
print(d['primary']) # Fetch the object if it is still alive

# Remove a reference and run GC
del a
gc.collect()

# Entry was automatically removed: Keyerror
print(d['primary'])
