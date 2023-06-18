#!/usr/bin/env python

# Set default argument value for the 2nd / 3rd argument
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'): # Test whether or not a sequence contains a certain value
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid use response')
        print(reminder)

# Give mandatory argument only
ask_ok('Do you really want to quit?')
# Give one of the optional argument
ask_ok('OK to overwrite the file?', 2)
# Give all arguments
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5
# Default value are evaluated at the point of function definition
def f(arg = i): # i = 5
    print(arg)

i = 6
f() # print 5

# The default value is evaluated only once
# It makes a difference when the default is a mutable object
# such as a list, dictionary, etc.
# The argument of this function will be accumulated
def lf(a, L=[]):
    L.append(a)
    return L

print(lf(1)) # [1]
print(lf(2)) # [1, 2]
print(lf(3)) # [1, 2, 3]

# This function will create a new list for each function call
def lf(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(lf(1)) # [1]
print(lf(2)) # [2]
print(lf(3)) # [3]

# Use keyward arguments with 'kwarg=value'
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                            # 1 positional argument
parrot(voltage=1000)                                    # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')               # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)               # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')           # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')    # 1 positional, 1 keyword

# The followings are invalid
# parrot()                    # Required argument missing
# parrot(voltage=5.0, 'dead') # Non-keyword argument after a keyword argument
# parrot(110, voltage=220)    # Duplicate value for the same argument
# parrot(actor='John Cleese') # Unknown keyword argument

# `**name` receives a dictionary containing all keyword arguments
# except for those corresponding to a formal parameter
# `*name` receives a tuple containing the positional arguments
# beyond the formal parameter list
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments: # Iterate a tuple of positional arguments
        print(arg)
    print("-" * 40)
    for kw in keywords: # Iterate a dictionary of keyword arguments
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Restriction of parameter passing
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
    # |           |  |           |  `- Keyword only
    # |           |  |           `- Keyword-only parameter
    # |           |  `- Positional or keyword (named parameters)
    # |           `- Positional-only parameter (> Python 3.8)
    # `- Positional only
    #
    # Without '/' or '*', arguments may be passed to the function
    # by positional or by keyword
    pass

# Familier form
def standard_arg(arg):
    print(arg)

standard_arg(2)
standard_arg(arg=2)

# Positional-only
def pos_only_arg(arg, /):
    print(arg)

pos_only_arg(1)
# pos_only_arg(arg=1) # TypeError

# Keyword-only
def kwd_only_arg(*, arg):
    print(arg)

# kwd_only_arg(3) # TypeError
kwd_only_arg(arg=3)

# Combination
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# combined_example(1, 2, 3) # TypeError
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError

# Function with positonal argument `name` and `**kwd` which has `name` as a key
def foo(name, **kwds):
    return 'name' in kwds

# The keyword "'name'"" will always bind to the first parameter
# foo(1, **{'name': 2}) # TypeError

# '/' makes 'name' as a positional argument and "'name'" will be a key
# in the keyword arguments
def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2}) # True

# Guidance:
# - Using positional-only:
#       parameter names no real meaning, enforce the order of the arguments to the user,
#       need to take some positional parameters and arbitary keywords,
# - Using keyword-only:
#       the name has meaning and it makes function definition more understandable,
#       prevent user relying on the position of the argument
# - API:
#       use positional-only to prevent breaking API changes for parameter's names

# Arbitrary argument lists
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args)) # `*args` will be wrapped up in a tuple

def concat(*args, sep="/"): # `*args` is followed by keyword-only parameters
    return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

# Unpacking argument lists
print(list(range(3, 6))) # Normal call with separate arguments
args = [3, 6]
print(list(range(*args))) # Call with arguments unpacked from a list

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d) # Unpack a dictionary

# Lambda expressions: create anonymous function of a single expression
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
# def f(x):
#     return x + 42
f(0)
f(1)

# Documentation strings (docstrings)
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    # 1st line: description, begin with a capital letter and end with a period
    # 2nd line: blank
    # 3rd line: calling conventions, side effects, etc.
    # ...
    # Indentation will be aligned with that of the first line
    pass

print(my_function.__doc__)


# Function annotations
def f(ham: str, eggs: str = 'eggs') -> str: # Type annotations
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')
