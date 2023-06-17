class MyClass:
    """A simple example class"""
    i = 12345

    def __init__(self):
        self.data = []

    def f(self):
        return 'hello world!'

x = MyClass() # Instantiation
print(x.i) # Attributes
print(x.data)
print(x.__doc__) # docstring
x.f() # Method

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

# Initialize with values
x = Complex(3.0, -4.5)
print(f"{x.r}, {x.i}")

x = MyClass()
# Data attribute can be appended to an instance
# like local variable
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

xf = x.f # Bind method object
print(xf()) # and call later

class Dog:
    kind = 'canine' # Class vairable shared by all instances

    def __init__(self, name):
        self.name = name # Instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind) # Shared by all dogs
print(e.kind)

print(d.name) # Unique to d
print(e.name) # Unique to e

class Dog:
    tricks = [] # Mutable object for class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks) # ['roll over', 'play dead'], Unexpectedly shared by all dogs

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = [] # Mutable object for instance variable

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')

d.add_trick('roll over')
e.add_trick('play dead')

print(d.tricks) # ['roll over']
print(e.tricks) # ['play dead']

