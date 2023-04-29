#!/usr/bin/env python

# Sets: sets of un-ordered unique data
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # Duplicates have been removed

# Test membership
print('orange' in basket)
print('crabgrass' in basket)

# Operation between 2 lists
a = set('abracadabra')
b = set('alacazam')
print(a) # Unique letters in a
print(b)
print(a - b) # Letters in a but not in b
print(a | b) # Letters in a or b or both
print(a & b) # Letters in both a and b
print(a ^ b) # Letters in a but not both

# Set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
