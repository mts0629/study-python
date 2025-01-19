#!/usr/bin/env python

from collections.abc import Iterable

def nums_below(numbers: Iterable[float], limit: float) -> list[float]:
    output = [] # Inferenced as list[float]
    for num in numbers:
        if num < limit:
            output.append(num)
    return output
