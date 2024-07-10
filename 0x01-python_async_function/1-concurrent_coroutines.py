#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2
int arguments (in this order): n and max_delay.
You will spawn wait_random n times with the specified
max_delay. wait_n should return the list of all
the delays (float values).
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine called wait_n that takes in 2
    int arguments (in this order): n and max_delay.
    You will spawn wait_random n times with the specified
    max_delay. wait_n should return the list of all
    the delays (float values).
    """
    stored_list: List[float] = []
    for _ in range(0, n):
        stored_list.append(await wait_random(max_delay))
    for i, _ in enumerate(stored_list):
        minimum = min(stored_list[i:])
        min_index = stored_list.index(minimum)
        temp = stored_list[i]
        stored_list[i] = minimum
        stored_list[min_index] = temp
    return stored_list
