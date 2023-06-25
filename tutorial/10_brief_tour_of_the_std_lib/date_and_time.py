#!/usr/bin/env python

from datetime import date

# Construct and print formatted date
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# Calendar arithmetic for dates
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)
