#!/usr/bin/env python

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            # break statements: breaks out of the innermost loop
            break
    # else clauses on loops:
    # be executed after a loop is finished without being terminated by break
    else:
        # Loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        # continue statements: go to the next iteration of a loop
        continue
    print("Found and odd number", num)
