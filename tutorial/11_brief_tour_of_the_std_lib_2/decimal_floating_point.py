#!/usr/bin/env python

from decimal import *

# Calculate 70 cent and 5% tax of it with Decimal and float
print(round(Decimal('0.70') * Decimal('1.05'), 2))  # '0.74'
print(round(.70 * 1.05, 2))                         # '0.73'

# Modulo with Decimal and float
print(Decimal('1.00') % Decimal('.10')) # '0.00'
print(1.00 % 0.10)                      # '0.09999999999999995'

# 0.1*10 with Decimal and float
print(sum([Decimal('0.1')]*10) == Decimal('1.0'))   # True
print(sum([0.1]*10) == 1.0)                         # False

# Calculate 1/7 with 36 digits after the decimal point
getcontext().prec = 36
print(Decimal(1) / Decimal(7))
