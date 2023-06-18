#!/usr/bin/env python

# Dictionary: set of key-value pair
# Values indexed by a unique key and the key is immutable
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127 # Append a key-value pair
print(tel)

print(tel['jack']) # Refer an item by the key

del tel['sape'] # Delete a key-value pair
tel['irv'] = 4127
print(tel)

print(list(tel)) # Get a list of keys
print(sorted(tel)) # Get a sorted list of keys

# Check key existence
print('guido' in tel)
print('jack' not in tel)

# dict() generates a dictionary with a list of tuples of key-value pair
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# Dictionary comprehension
print({x: x**2 for x in (2, 4, 6)})

# dict() with keyword arguments
print(dict(sape=4139, guido=4127, jack=4098))
