#!/usr/bin/env python

# Tuple
t = 12345, 54321, 'hello!'
print(t[0]) # THe first element
print(t)

# Tuples can be nested
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuples are immutable
# t[0] = 888888 # TypeError

# But they can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = () # An empty tuple
print(empty, f"len={len(empty)}")

singleton = 'hello', # A tuple with a single item, ',' is required
print(singleton, f"len={len(singleton)}")

# Sequence unpacking
x, y, z = t
print(x, y, z)
# x, y = t # ValueError, this tuple has 3 items
