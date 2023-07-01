#!/usr/bin/env python

def primitives() -> None:
    i: int = 1
    f: float = 1.0
    b: bool = True
    s: str = "test"
    B: bytes = b"test"


def collections_v3_9() -> None:
    # For collections on Python 3.9+
    l: list[int] = [1]
    s: set[int] = {6, 7}
    d: dict[str, float] = {"field": 2.0}
    tf: tuple[int, str, float] = (3, "yes", 7.5) # Tuples of fixed size
    tv: tuple[int, ...] = (1, 2, 3) # Tuples of variable size


from typing import List, Set, Dict, Tuple

def collections_v3_8() -> None:
    # For collections on Python 3.8 and earlier
    l: List[int] = [1]
    s: Set[int] = {6, 7}
    d: Dict[str, float] = {"field": 2.0}
    tf: Tuple[int, str, float] = (3, "yes", 7.5)
    tv: Tuple[int, ...] = (1, 2, 3)

from typing import Union, Optional

def few_types() -> None:
    # On Python 3.10+, use the | operator when something could be one of a few types
    l_3_10: list[int | str] = [3, 5, "test", "fun"]
    # Use Union on earler versions
    l_3_9: list[Union[int, str]] = [3, 5, "test", "fun"]

def optionals(condition: bool) -> None:
    # Use Optional[X] for a value that could be None
    # Optional[X] is the same as
    # X | None or Union[X, None]
    x: Optional[str] = "something" if condition else None
    if x is not None:
        # mypy understands x won't be None here because of the if-statement
        print(x.upper())

    # Or, a value can never be None due to some logic that mypy doesn't understand,
    # use an assert
    assert x is not None
    print(x.upper())

