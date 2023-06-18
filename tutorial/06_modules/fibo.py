#!/usr/bin/env python

# Fibonacci numbers module

def fib(n):
    """Write Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    """Return Fibonacci series up to n"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


# This code makes this module executable when it is executed as a "main" file via command line
# The code isn't executed by `import`
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

    # A list of built-in modules
    print(sys.builtin_module_names)

    # Module search path
    # It is initialized as:
    # - The directory containing input script
    # - PYTHONPATH
    # - The installation-dependent default (customary including `site-packages` directory)
    print(sys.path)

    # Compiled modules are cached as `module.version.pyc` in a `__pycache__` directory
    # e.g.) __pycache__/spam.cpython-33.pyc
