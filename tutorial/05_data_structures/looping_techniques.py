#!/usr/bin/env python

# Loop for key-value pairs in the dictionary
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# Loop for indices and elements of the sequence
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# Loop for 2 sequences
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# Loop in reverse order
for i in reversed(range(1, 10, 2)):
    print(i, end=',')
print()

# Loop in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i, end=',')
print()

for i in basket:
    print(i, end=',') # The original sequence is not changed
print()

# Remove duplicates
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i, end=',')
print()

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
print(raw_data)
# Sometimes create a new list is better than modify the original list
filtered_data = [value for value in raw_data if not math.isnan(value)]
print(filtered_data)
