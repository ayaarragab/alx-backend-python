#!/usr/bin/env python3

"""
This module provides a function to
convert a key-value pair into a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts the given key-value pair into a tuple.

    Args:
        k (str): The key.
        v (int | float): The value.

    Returns:
        tuple: A tuple containing the key-value pair.
    """
    return (k, v)
