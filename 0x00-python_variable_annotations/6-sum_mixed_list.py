#!/usr/bin/env python3
"""
A module that provides a type-annotated function to return the sum of a mixed list of integers and floats.
"""

from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a mixed list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
        float: The sum of all numbers in the list as a float.
    """
    return float(sum(mxd_lst))
