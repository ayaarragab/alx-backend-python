#!/usr/bin/env python3
"""
a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers.

    Args:
        mxd_lst (List[int]): A list containing integers.

    Returns:
        float: The sum of the integers in the list.

    """
    return float(sum(mxd_lst))
