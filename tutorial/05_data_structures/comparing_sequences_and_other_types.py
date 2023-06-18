#!/usr/bin/bash python

# Comparing sequence objects with the same sequence type
# Following conditions return True
print((1, 2, 3) < (1, 2, 4)) # Ordered by an element at the same position in 2 sequences
print([1, 2, 3] < [1, 2, 4])
print((1, 2, 3, 4) < (1, 2, 4))
print('ABC' < 'C' < 'Pascal' < 'Python') # Strings are compared with lexicographical ASCII ordering
print((1, 2) < (1, 2, -1)) # The shorter one is smaller
print((1, 2, 3) == (1.0, 2.0, 3.0)) # Comparing different number types by its equality
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))

# If there are no arbitrary order between compared items, TypeError is raised
