#!/usr/bin/env python

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']

# Membership test
print('apple' in fruits)
print('grape' not in fruits)

# Equivalent test
print(fruits[0] is 'orange')
print(fruits[0] is not 'apple')

# Short-circuit: evaluation stops as soon as the result is determined
print('apple' in fruits or 'grape' in fruits) # Stop at `'apple' in fruits`
print('grape' in fruits and 'apple' in fruits) # Stop at `'grape' in fruits`

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
# Assign the result of a boolean expression to a variable
non_null = string1 or string2 or string3
print(non_null)
