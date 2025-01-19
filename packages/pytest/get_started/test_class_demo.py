#!/usr/bin/env python
"""Test by class sharing the same instance."""

class TestClassDemoInstance:
    value = 0   # Class attribute

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 1  # The same instance is shared with `test_one`
