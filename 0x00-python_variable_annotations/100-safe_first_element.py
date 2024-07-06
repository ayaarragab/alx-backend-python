#!/usr/bin/env python3

"""
This module contains a function to safely
retrieve the first element of a list.
"""
from typing import Sequence, Any, Union
from types import NoneType


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Returns the first element of a list if it exists,
    otherwise returns None.

    Args:
        lst (list): The input list.

    Returns:
        The first element of the list if it exists,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
