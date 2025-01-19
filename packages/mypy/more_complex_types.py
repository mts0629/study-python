#!/usr/bin/env python

from collections.abc import Iterable
# or "from typing import Iterable"

from typing import Union

def greet_all_list(names: list[str]) -> None:
    for name in names:
        print('Hello ' + name)

names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]
greet_all_list(names)
greet_all_list(ages) # Error due to incompatible types

def greet_all(names: Iterable[str]) -> None:
    for name in names:
        print('Hello ' + name)

# Works for iterables
greet_all(("Alice", "Bob", "Charlie",))
greet_all({"Alice", "Bob", "Charlie",})

def normalize_id(user_id: Union[int, str]) -> str:
    if isinstance(user_id, int):
        return f'user-{100_000 + user_id}'
    else:
        return user_id

# Accepts ints or strings
normalize_id(100)
normalize_id('100')
