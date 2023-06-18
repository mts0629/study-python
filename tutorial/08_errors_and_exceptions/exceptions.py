#!/usr/bin/env python

# Exceptions
for expression in (
    "10 * (1 / 0)",         # ZeroDivisionError
    "4 + spam * 3",         # NameError
    "'2' + 2",              # TypeError
    "12345.6789 ** 1000",   # OverflowError
    "assert 1 == 0",        # AssertionError
    "arr = [1, 2]; arr[3]"  # IndexError
    # ...
):
    try:
        exec(expression)
    except Exception as err:
        print(f"{type(err)}: {err}")
