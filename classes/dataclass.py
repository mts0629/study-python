#!/usr/bin/env python

from dataclasses import dataclass

# Data structure like a C struct by dataclasses.dataclass
@dataclass(frozen=True) # Set as immutable
class Employee:
    name: str
    dept: str
    salary: int

    # __init__() is appended internally

john = Employee('john', 'computer lab', 1000)
print(john.dept)
print(john.salary)

print(john)
