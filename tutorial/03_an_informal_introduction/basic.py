#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" utf-8 is default encoding """

def main():
    # Calculation
    print("2 + 2 = ", (2 + 2))
    print("50 - 5 * 6 = ", (50 - 5 * 6))
    print("(50 - 5 * 6) / 4 = ", ((50 - 5 * 6) / 4))
    print("(8 / 5) = ", (8 / 5))

    print("17 / 3 = ", (17 / 3))  # Classic division
    print("17 // 3 = ", (17 // 3)) # Floor division
    print("17 % 3 = ", (17 % 3))  # Remainder of the division
    print("5 * 3 + 2 = ", (5 * 3 + 2)) # Floored quotient * divisor + remainder

    print("(5 ** 2) = ", (5 ** 2)) # 5 squared
    print("(2 ** 7) = ", (2 ** 7)) # 2 to the power of 7

    width = 20
    height = 5 * 9
    print("width * height = ", width * height)

    # 'n' is undefined, error
    # print("n = ", n)

    # Floating point
    print("4 * 3.75 - 1 = ", (4 * 3.75 - 1))

    # In the interactive mode, the last output is stored to '_'
    # >>> tax = 12.5 / 100
    # >>> price = 100.50
    # >>> price * tax
    # 12.5625
    # >>> price + _
    # 113.0625
    # >>> round(_, 2)
    # 113.06

    # Complex number
    print(3 + 5j)


    # String
    print('spam eggs')
    print("spam eggs")
    print('doesn\'t')
    print("doesn't")
    print('"Yes," they said.')
    print("\"Yes,\" they said.")
    print('"Isn\'t," they said.')
    # In the interactive mode: '"Isn\'t," they said.'

    s = 'First line.\nSecond line.'
    # Without print(), \n is included in the output
    print(s) # With print(), \n produces a new line

    print("C:\some\name")
    print(r"C:\come\name") # Raw string

    # String literal with multi lines
    print("""\
Usage: thingy [OPTIONS]
    -h                  Display this usage message
    -H hostname         Hostname to connect to

""")

    # 3 times 'un', followed by 'ium'
    print(3 * "un" + "ium")

    # Concatenation
    print("Py" "thon")

    text = ("Put several strings within parentheses "
            "to have them joined together.")
    print(text)

    prefix = 'Py'
    #print(prefix 'thon')   # Can't concatenate a variable and a string literal
                            # SyntexError: invalid syntax
    print(prefix + 'thon')  # '+' operator is valid

    word = 'Python'
    print(word[0])  # Character in position 0
    print(word[5])  # Character in position 5

    print(word[-1]) # Last character
    print(word[-2]) # Second-last character
    print(word[-6])

    # Slicing: [(start index, included):(end index, excluded)]
    print(word[0:2])    # Characters from position 0 (included) to 2 (excluded)
    print(word[2:5])    # Characters from position 0 (included) to 5 (excluded)

    print(word[:2] + word[2:])  # (0 to 1) + (2 to end) = word
    print(word[:4] + word[4:])  # (0 to 3) + (4 to end) = word

    # print(word[42])    # IndexError

    # Slicing can deal with
    print(word[4:42])
    print(word[42:])

    # String is immutable
    # word[0] = 'J'     # TypeError
    # word[2:] = 'py'   # TypeError

    # Need to create new string
    print('J' + word[1:])
    print(word[:2] + 'py')

    # Length of string
    s = 'supercalifragilisticexpialidocious'
    print(len(s))


    # List
    squares = [1, 4, 9, 16, 25]
    print(squares)

    # Indexing, slicing
    print(squares[0])
    print(squares[-1])
    print(squares[-3:])

    # Return new list with shallow copy (copy by reference)
    print(squares[:])

    # Concatenation
    print(squares + [36, 49, 64, 81, 100])

    # List is mutable
    cubes = [1, 8, 27, 65, 125] # Something's wrong here
    cubes[3] = 64 # The cube of 4 is 64
    print(cubes)

    # Append an item to the tail
    cubes.append(216)
    cubes.append(7 ** 3)
    print(cubes)

    # Assignment to sliced list
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    print(letters)

    letters[2:5] = ['C', 'D', 'E']
    print(letters)

    letters[2:5] = []
    print(letters)

    letters[:] = []
    print(letters)

    # Length
    letters = ['a', 'b', 'c', 'd']
    print(len(letters))

    # Nested list
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)
    print(x[0])
    print(x[0][1])

    # Fibonacci series
    a, b = 0, 1
    while a < 100:
        print(a, end=',')
        a, b = b, (a + b)
    print('')


if __name__ == "__main__":
    main()
