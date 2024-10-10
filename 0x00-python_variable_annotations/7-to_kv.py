#!/usr/bin/env python3
"""
A module that provides a type-annotated function to create a tuple from a string and a number.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple containing the string k and the square of v.

    Args:
        k (str): The string value.
        v (Union[int, float]): The integer or float value.

    Returns:
        Tuple[str, float]: A tuple where the first element is k and the second is the square of v.
    """
    return (k, float(v ** 2))
