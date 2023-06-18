#!/usr/bin/env python

# range function
# Generate sequence from 0 to 4
for i in range(5):
    print(i)

# (start, end)
print(list(range(5, 10)))
# (start, end, step)
print(list(range(0, 10, 3)))
print(list(range(-10, -100, -30)))

# Iteration by generated sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# range doesn't  generate a list but an iterable (object)
print(range(10))

# sum() returns the sum of an iterable
print(sum(range(4)))
