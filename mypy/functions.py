#!/usr/bin/env python

from typing import Callable, Iterator, Union, Optional

def strigify(num: int) -> str:
    return str(num)

def plus(num1: int, num2: int) -> int:
    return num1 + num2

# Does not return value, and default value is used for an argument
def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)

# Dynamically typed (treated as Any)
# and that functions without any annotations not checked
def untyped(x):
    x.anything() + 1 + "string"

# Callable (function) value
def f(x: int, y: float) -> float:
    return x + y

x: Callable[[int, float], float] = f

def register(callback: Callable[[str], int]) -> None:
    pass

# Generator function that yields ints
def gen(n: int) -> Iterator[int]:
    i = 0;
    while i < n:
        yield i
        i += i

# Annotation over multiple lines
def send_email(address: Union[str, list[str]],
               sender: str,
               cc: Optional[list[str]],
               bcc: Optional[list[str]],
               subject: str = '',
               body: Optional[list[str]] = None
               ) -> bool:
    pass
    return True


# Positional-only and keyword-only arguments
def quux(x: int, /, *, y: int) -> None:
    pass

quux(3, y=5)
quux(3, 5)      # error: Too many positional arguments for "quux"
quux(x=3, y=5)  # error: Unexpected keyword argument "x" for "quux"

def make_request(*args: str, **kwargs: str) -> dict[str, str]:
    return {"key": "value"}

class SomeClass:
    def do_api_query(self, request: dict[str, str]) -> str:
        return "foobaz"

    # This says each positional arg and each keyword arg is a "str"
    def call(self, *args: str, **kwargs: str) -> str:
        reveal_type(args)   # Revealed type is "builtins.tuple[builtins.str, ...]"
        reveal_type(kwargs) # Revealed type is "builtins.dict[builtins.str, builtins.str]"
        request = make_request(*args, **kwargs)
        return self.do_api_query(request)
