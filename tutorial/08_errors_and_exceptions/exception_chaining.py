#!/usr/bin/env python

# If an unhandled exception occurs inside an except section,
# it will be attached to current on and included in the error message
#
# FileNotFoundError occurs while RuntimeError beging handled
# try:
#     open("database.sqlite")
# except OSError:
#     raise RuntimeError("unable to handle error")
#

# Indicate that an exception is derived from another one by `from`
# exc = FileNotFoundError()
# raise RuntimeError from exc

# Transform a ConnectionError to RuntimeError
# def func():
#     raise ConnectionError
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

# Disable automatic exception chaining by `from None`
try:
    open('database.sqlite')
except OSError:
    raise RuntimeError from None
