#!/usr/bin/env python3
'''
element of the list
'''
from typing import List, TypeVar, Optional

T = TypeVar('T')

def safe_first_element(lst: List[T]) -> Optional[T]:
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
