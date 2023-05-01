#!/usr/bin/env python

# Import module, add a module name into the namespace
import fibo

# Access functions in the 'fibo' module
fibo.fib(1000)
print(fibo.fib2(1000))

# Show a module name
print(fibo.__name__)

# Assign to a local variable
fib = fibo.fib
fib(500)

# Import names from a module directly into the importing module's namespace
from fibo import fib, fib2
fib(500)
print(fib2(500))

# Import all names that a module defines
from fibo import *
fib(500)

# Bind a module to a name following to `as`
import fibo as fib
fib.fib(500)

# Import a name in the module and bind it to a specific name
from fibo import fib as fibonacci
fibonacci(500)
