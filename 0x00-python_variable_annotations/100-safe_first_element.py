#!/usr/bin/env python3
"""
Module that annotates below function parameters
and returns values with appropriate types.
"""
from typing import Sequence, Any, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, otherwise returns None.

    Args:
        lst (List[T]): A list of elements of any type.

    Returns:
        Optional[T]: The first element of the list or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
