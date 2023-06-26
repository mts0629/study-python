#!/usr/bin/env python

from array import array

# Create an array of unsigned 2-byte integers
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

# deque object for queueing
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# Pseudo code for breath first search (BFS) by deque
# unsearced = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearced.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearced.append(m)

import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# Bisect insertion for sorted sequence
bisect.insort(scores, (300, 'ruby'))
print(scores)

from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)       # Rearrange the list into heap order
heappush(data, -5)  # Add a new entry
# Fetch the three smallest entries
print([heappop(data) for i in range(3)]) 
