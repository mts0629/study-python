#!/usr/bin/env python
"""Test multiple tests in a class."""

class TestClass:    # Test class is prefixed with `Test`
    def test_one(self): # Test case (prefixed with `test_`)
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")  # Fail

