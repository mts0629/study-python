#!/usr/bin/env python

def greeting(name: str) -> str:
    return 'Hello' + name

greeting('Alice')
# Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
greeting(b'Bob')
# Argument 1 to "greeting" has incompatible type "int"; expected "str"
greeting(123)

def bad_greeting(name: str) -> str:
    # Unsupported operand types for * ("str" and "str")
    return 'Hello' * name
