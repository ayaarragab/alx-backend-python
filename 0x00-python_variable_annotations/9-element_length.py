#!/usr/bin/env python3
"""
function’s parameters and return values
with the appropriate types
"""
from typing import Iterable, List, Tuple, Sequence


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the given list.

    Args:
        lst: A list of sequences.

    Returns:
        A list of tuples, where each tuple contains
        a sequence from the input list
        and its corresponding length.

    """
    return [(i, len(i)) for i in lst]
