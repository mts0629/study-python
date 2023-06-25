#!/usr/bin/env python

from timeit import Timer

# Compare elapsed time of swapping variables by ...
# Using temoporal variable
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# Using unpacking of a tuple
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
