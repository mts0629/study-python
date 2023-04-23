#!/usr/bin/env python

# Define a function
def fib(n): # Write Fibonacci series up to n
    # docstring
    """
    Print a Fibonacci series up to n.
    """
    # Local variables are stored in a new symbol table
    # Also arguments are introduced into the table (call-by-value)
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Calling a function
fib(2000)

# The name of the function is introduced into the current symbol table
# and an interpreter recognizes an object which is indicated with that name as user-defined function
print(fib)
f = fib
f(100)

# A function without return statements returns "None" actually
fib(0) # No outputs
print(fib(0))

# Define a function which returns a list
def fib2(n): # Return Fibonacci series up to n
    """
    Return a list containing the Fibonacci series up to n.
    """
    result = []
    a, b = 0, 1
    while a < n:
        # Call a method: list.append()
        result.append(a)
        a, b = b, a + b
    return result

f100 = fib2(100)
print(f100)
