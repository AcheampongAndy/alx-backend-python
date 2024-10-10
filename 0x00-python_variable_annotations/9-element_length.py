from typing import List, Tuple, Any

def element_length(lst: List[Any]) -> List[Tuple[Any, int]]:
    """
    Returns a list of tuples, each containing an element from the input list and its length.

    Args:
        lst (List[Any]): A list of elements (of any type).

    Returns:
        List[Tuple[Any, int]]: A list of tuples, where each tuple contains an element and its length.
    """
    return [(i, len(i)) for i in lst]
