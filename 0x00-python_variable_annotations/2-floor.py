#!/usr/bin/env python3
"""
A module that provides a type-annotated function to return the floor of a float.
"""

import math

def floor(n: float) -> int:
    """
    Returns the floor of the float n.

    Args:
        n (float): The float number.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
