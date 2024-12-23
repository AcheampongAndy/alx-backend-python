#!/usr/bin/env python3
"""
A module that provides a type-annotated function to return the sum of a list of floats.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The sum of all float numbers in the list.
    """
    return sum(input_list)
