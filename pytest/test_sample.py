#!/usr/bin/env python
"""test_sample.py"""


def inc(x: int) -> int:
    """Increment an argument."""
    return x + 1


def test_inc() -> None:
    """Test increment."""
    assert inc(3) == 5  # Wrong

