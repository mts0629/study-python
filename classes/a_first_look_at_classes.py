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
