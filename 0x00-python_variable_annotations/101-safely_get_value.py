#!/usr/bin/env python3
'''
module that retrieves
'''
from typing import TypeVar, Dict, Optional, Any

K = TypeVar('K')  # Type variable for keys
V = TypeVar('V')  # Type variable for values

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    """
    Safely retrieves a value from a dictionary based on the given key.

    Args:
        dct (Dict[K, V]): The dictionary to retrieve the value from.
        key (K): The key to look for in the dictionary.
        default (Optional[V]): The value to return if the key is not found (default is None).

    Returns:
        Optional[V]: The value associated with the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
