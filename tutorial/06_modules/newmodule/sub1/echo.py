#!/usr/bin/env python

def put(string: str) -> None:
    """Put echo string."""
    global echo_string_
    echo_string_ = string

def get() -> str:
    """Get echo string."""
    return echo_string_
