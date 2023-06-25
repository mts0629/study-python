#!/usr/bin/env python

import math

# cos(PI/4)
print(math.cos(math.pi / 4))
# log_2(1024)
print(math.log(1024, 2))

import random

# Random choice
for _ in range(3):
    print(random.choice(['apple', 'pear', 'banana']))

# Random sampling from a sequence
print(random.sample(range(100), 10))

# Get random float in [0, 1)
for _ in range(3):
    print(random.random())

# Get random integer chosen from the range
for _ in range(3):
    print(random.randrange(6))

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

# Mean, median, variance of the iterable object
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))
