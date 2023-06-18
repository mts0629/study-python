#!/usr/bin/env python

# match statements (>= Python 3.10):
# takes an expresssion and compares its value to following case blocks
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        # Combine literals with "|"
        # case 401 | 403 | 404:
        #     return "Not allowed"
        case _: # Wildcard
            return "Something's wrong with the internet"

print(http_error(400))
print(http_error(420))

def verify_point(point):
    # Patterns can look like unpacking assignments
    # and can be used bind variables
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            raise ValueError("Not a point")

verify_point((0, 0))
verify_point((3, 1))

class Point:
    x: int
    y: int
    # Special attributes for class pattern (>= Python 3.10)
    __match_args__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    # For classes, class name with an argument list resembling a constructor
    # can be used
    match point:
        # positional parameters can be used
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        # For a special attribute set by `__match_args__ = ("x", "y")`
        case Point(y=var, x=1):
            print(f"X=1 and Y={var}")
        case Point():
            print("Somewhere else") 
        case _:
            print("Not a point")

where_is(Point(0, 0))
where_is(Point(1, 2))

# Patterns can be nested
def where_are(points):
    match points:
        # For a list of Point
        case []:
            print("Not points")
        case [Point(x=0, y=0)]:
            print("The origin")
        case [Point(x=x, y=y)]:
            print(f"Single point {x}, {y}")
        case [Point(x=0, y=y1), Point(x=0, y=y2)]:
            print(f"Two on the Y axis at {y1}, {y2}")
        case _:
            print("Something else")

where_are([])
where_are([Point(1, 2)])
where_are([Point(0, 2), Point(0, 4)])

def is_diagonal(point):
    match point:
        # Add if clause to a pattern as a "guard"
        # If the guard is false, match goes on to try the next case block
        case Point(x=x, y=y) if x == y: # Values are captured before the guard is evaluated
            print(f"Y=X at {x}")
        case Point(x, y):
            print(f"Not on the diagonal")

is_diagonal(Point(1, 1))
is_diagonal(Point(0, 1))

from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'

def emote_by_color(color):
    match color:
        # Use named constant for patterns
        case Color.RED:
            print("I see red!")
        case Color.GREEN:
            print("Grass is green")
        case Color.BLUE:
            print("I'm feeling the blues :(")

color = Color(
    input("Enter your choice of 'red', 'blue' or 'green': ")
)
emote_by_color(color)
