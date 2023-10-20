#!/usr/bin/env python

# Formatted string literals (`f-strings`)
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')

# Formatting by str.format() and formatting directives
yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

s = 'Hello, world.'
# str(): return a string version of an object (human-readable)
print(str(s))
# repr(): return a string containing a printable representation of an object
# (can be read by the interpreter)
print(repr(s))

# The same expressions are returned by both of the str() and repr()
print(str(1/7))
print(repr(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

hello = 'hello, world\n'
# The repr() of a string adds string quotes and backslashes
hellos = repr(hello)
print(hellos)

# Details of f-strings
# The argument of repr() may be any Python object
print(repr((x, y, ('spam', 'eggs'))))

import math
print(f'The value of pi is approximately {math.pi:.3f}.') # Specify rounding digits

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}') # Specify a minimum number of characters wide

animals = 'eels'
print(f'My hovercraft is full of {animals}.')
print(f'My hovercraft is full of {animals!a}.') # Apply `ascii()`
print(f'My hovercraft is full of {animals!s}.') # Apply `str()`
print(f'My hovercraft is full of {animals!r}.') # Apply `repr()`

bugs = 'roaches'
count = 13
area = 'living room'
 # `=` expands an expression to:
 # `(the text of expression) = (the representation of the evaluated expression)`
print(f'Debugging {bugs=} {count=} {area=}')

# String format() methods
# Basic usage
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# A number in the brackets can be used to refer  the position of the passed objects of the method
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

# Refer by the name of the arguments
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1} and {other}.'.format('Bill', 'Manfred', other='Georg'))

# Refer dictionary with its keys by `[]`
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# Refer dictionary as the keyword arguments
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print('{0:2d}, {1:3d}, {2:4d}'.format(x, x*x, x*x*x))

# Manually string formatting
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ') # rjust(): right-justify a string by padding with space
    # A line doesn't end
    print(repr(x*x*x).rjust(4))

# String justifications
print('---------------')
print('justified'.rjust(15))
print('justified'.ljust(15)) # Left-justify
print('justified'.center(15)) # Centering
print('---------------')

# `zfill()`: pad a numeric string on the left with zeros
print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))

# Old string formatting
print('The value of pi is approximately %5.3f.' % math.pi)
