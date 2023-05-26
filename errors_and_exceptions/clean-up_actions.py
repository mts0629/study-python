#!/usr/bin/env python

# `finally` clause executes the last task before the `try` statement
# completes
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

# Return from the finally clause
def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return()) # False

# finally clause is always executed
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)        # try -> else -> finally
divide(2, 0)        # try -> except -> finally
divide("2", "1")    # try -> finally -> raise TypeError
