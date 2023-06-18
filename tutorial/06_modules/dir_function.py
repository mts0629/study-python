#!/usr/bin/env python

import fibo, sys

# Find out which names a module `fibo` defines
# It returns a sorted list of strings
print(dir(fibo))

print(dir(sys))

a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib

# Without argumetns, it lists the names currently defined
# All types of names: variables, modules, functions, etc.
print(dir())

# To list built-in functions and variables, import `builtins`
import builtins
print(dir(builtins))
