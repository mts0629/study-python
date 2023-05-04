#!/usr/bin/env python

# Relative imort
from ..sub1.echo import echo_string_

def get_twice() -> str:
    """Get a list of echo strings twice."""
    return [echo_string_, echo_string_]
