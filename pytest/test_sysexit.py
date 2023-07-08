#!/usr/bin/env python
"""Test assertion of an exception."""

import pytest


def f() -> None:
    """Raise SystemExit(1)."""
    raise SystemExit(1)


def test_sysexit() -> None:
    """Test that SystemExit(1) is raised."""
    with pytest.raises(SystemExit):
        f()

