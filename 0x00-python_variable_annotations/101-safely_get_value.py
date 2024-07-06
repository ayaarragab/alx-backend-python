#!/usr/bin/env python3
"""
def safely_get_value(dct, key, default=None):
"""
from typing import Sequence, Any, Union, TypeVar, Mapping
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]) -> Union[Any, T]:
    """
    Safely retrieves the value associated with the
    given key from the dictionary.

    Args:
        dct (dict): The dictionary to retrieve the
        value from.
        key: The key to look for in the dictionary.
        default: The default value to return if
        the key is not found in the dictionary.

    Returns:
        The value associated with the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
