#!/usr/bin/env python
"""test_sample.py"""


def inc(x: int) -> int:
    """Increment an argument."""
    return x + 1


def test_inc() -> None: # Test case is prefixed with `test_`
    """Test increment."""
    assert inc(0) == 1


def test_inc_fail() -> None:
    """Test increment."""
    assert inc(3) == 5  # Wrong

