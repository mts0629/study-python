#!/usr/bin/env python

# More list operations
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)

# Count specified item
print(fruits.count('apple'))
print(fruits.count('tangerine'))

# Get an index of the specified item
print(fruits.index('banana'))
print(fruits.index('banana', 4)) # Find next banana starting at position 4

# Reverse the elements in the list
fruits.reverse()
print(fruits)

# Add an item to the end of the list
fruits.append('grape')
print(fruits)

# Sort the items in the list
fruits.sort()
print(fruits)

# Remove the last item from the list
print(fruits.pop())
print(fruits)
