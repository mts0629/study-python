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

# Using lists as stacks with append() and pop() (LIFO)
stack = [3, 4, 5]

stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack.pop())
print(stack)

# Using lists as queues is not efficient
# because operations to the first item: insert() and pop() are slow (FIFO)
# collections.deque is a better way
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  # Terry arrives
print(queue)
queue.append("Graham") # Graham arrives
print(queue)
queue.popleft()        # The first to arrive now leaves
print(queue)
queue.popleft()        # The second to arrive now leaves
print(queue)           # Remaining queue in order of arrival

# List comprehensions
# Making a list of squares
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
print(x) # x remains after the above loop

# Another way to create the same list
squares.clear()
squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares.clear()
squares = [x**2 for x in range(10)]
print(squares)

# List comprehension consists of brackets containing
# expression, for clause and 0 or more for / if clause
# It returns a new list resulting from evaluation of the expression
print(
    [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
)
# The above list is same with the follows
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
# Double values
print([x*2 for x in vec])
# Filter the list to exclude negative numbers
print([x for x in vec if x >= 0])
# Apply a function to all the elements
print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry', 'passion fruit  ']
# Call a method on each element
print([weapon.strip() for weapon in freshfruit])

# Create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])

# Flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
# List expression can contain complex expressions and nested functions
print([str(round(pi, i)) for i in range(1, 6)])

# Nested list comprehensions
# 3x4 matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Transpose the matrix
print([[row[i] for row in matrix] for i in range(4)])

# Equivalent code #1
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# Equivalent code #2
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

# Using a built-in function: '*' is unpacking of argument lists
print(list(zip(*matrix)))
