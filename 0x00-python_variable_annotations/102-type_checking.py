from typing import List, Tuple, Union

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zooms in on the tuple by repeating each element based on the zoom factor.

    Args:
        lst (Tuple[int, ...]): The input tuple.
        factor (int): The zoom factor (default is 2).

    Returns:
        List[int]: A list with the elements of the tuple repeated according to the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
