#!/usr/bin/env python

import reprlib

# Show a representation of the object by shorthand version
print(reprlib.repr(set('supercaligrailisticexpialidocious')))

import pprint

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
# Pretty printing
pprint.pprint(t, width=30)

import textwrap

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

# Reformat a single paragraph to specified width
print(textwrap.fill(doc, width=40))

import locale

# Set locale of the system
locale.setlocale(locale.LC_ALL, 'en_US.utf8')
# Get a mapping of conventions
conv = locale.localeconv()
print(conv)
# Print a currency in US format
x = 1234567.8
# print(locale.format("%d", x, grouping=True)) # DeplicationWarning
print(locale.format_string("%s%.*f",
                           (conv['currency_symbol'], conv['frac_digits'], x),
                           grouping=True))
