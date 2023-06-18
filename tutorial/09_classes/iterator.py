#!/usr/bin/env python

s = 'abc'
it = iter(s) # iter() returns an iterator object
print(it)
try:
    print(next(it)) # The iterator object proceeds by next()
                    # which returns __next__() method
    print(next(it))
    print(next(it))
    print(next(it))
except Exception as e:
    print(type(e)) # When there is no more element in the object,
                   # StopIteration is thrown

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self): # __iter__() returns an object which has __next__()
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char) # 'm' -> 'a' -> 'p' -> 's'
