#!/usr/bin/env python

class BaseClass:
    def __init__(self, x):
        self.value = x

    def print(self):
        print(f'Base: {self.value}')

# Define derived class
class DerivedClass(BaseClass):
    # Override an instance method
    def print(self):
        print(f'Derived: {self.value}')

    def print_twice(self):
        for _ in range(2):
            BaseClass.print(self) # Call a method of the base class

b = BaseClass(10)
d = DerivedClass(20) # BaseClass.__init__() is called

b.print()
d.print()
d.print_twice()

print(isinstance(b, BaseClass)) # Check the type of an instance
print(isinstance(d, BaseClass))
print(issubclass(DerivedClass, BaseClass)) # Check the inheritance relation

class AnotherBaseClass:
    def multiply(self, y):
        self.value *= y

# Multiple inheritance
class DerivedClassFromTwo(BaseClass, AnotherBaseClass):
    pass

d = DerivedClassFromTwo(5)
d.print() # From BaseClass
d.multiply(2) # From AnotherBaseClass
d.print()
