#!/usr/bin/env python

# SyntaxError: invalid syntax
# while True print('Hello world')

# Exceptions
# ZeroDivisionError
# 10 * (1/0)
# NameError
# 4 + spam * 3
# TypeError
# '2' + 2

while True:
    # Exception handling: try-except clause
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again ...")
    except (RuntimeError, TypeError, NameError): # Multiple exceptions
        pass

class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

# An except clause listing a derived class is not compatible
# with a base class
# Print "B", "C", "D"
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# Print "B", "B", "B", the first matching except clause is triggered
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")

try:
    raise Exception('spam', 'eggs')
except Exception as inst: # Bind exception to `inst`
    print(type(inst))   # The exception type
    print(inst.args)    # Arguments stored in .args
    print(inst)         # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
    x, y = inst.args    # Unpack args
    print('x =', x)
    print('y =', y)

# BaseException: common base class
#   |- Exception: non-fatal exceptions
#   |- SystemExit
#   |- KeyboardInterrupt
#   ...

