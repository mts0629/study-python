#!/usr/bin/env python
"""Test with a unique temporary directory."""

def test_needsfiles(tmp_path):  # `tmp_path` is a pytest fixture for temporary directory path
    print(tmp_path)
    assert 0

# Built-in pytest fixtures can be found out by: `pytest --fixtures`

