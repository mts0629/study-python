#!/usr/bin/env python

from dataclasses import dataclass

# Generators
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index] # yield return data for each time of next() calling
                          # and resume the last state

    # __iter__(), __next__() are created automatically
    # and StopIteration is also raised automatically

for char in reverse('golf'):
    print(char) # 'f' -> 'l' -> 'o' -> 'g'

# Generator expressions
print(sum(i*i for i in range(10))) # Sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x, y in zip(xvec, yvec))) # Dot product

page = [
    'The quick brown fox jumps over the lazy dog.',
    'The quick silver fox jumps over the lazy dog.',
    'The quick brown fox jumps over the lazy rabbit.',
]
# Unique words in the sentences
unique_words = set(word for line in page for word in line.split())
print(unique_words)

@dataclass
class Student:
    name: str
    gpa: float

graduates = [
    Student('Alice', 3.5),
    Student('Bob', 2.9),
    Student('Carol', 4.1)
]
# Student whose GPA is top
valedictorian = max((student.gpa, student.name) for student in graduates)
print(valedictorian)

# Reverse characters
data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))
