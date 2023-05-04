#!/usr/bin/env python

# Inport an `echo` submodule from the `newmodule` package
import newmodule.sub1.echo

# Refer a function from the loaded module
newmodule.sub1.echo.put("Hello")
print(newmodule.sub1.echo.get())

# Import the `echo` submodule
from newmodule.sub1 import echo
echo.put("Hello")
print(echo.get())

# Import the desired function `echo` from the submodule
from newmodule.sub1.echo import put, get 
put("Hello")
print(get())

from newmodule.sub2.echo import get_twice
print(get_twice())
