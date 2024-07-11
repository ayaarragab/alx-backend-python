#!/usr/bin/env python3
"""
Doc for task_wait_n
"""
from asyncio import run
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Doc for task_wait_n
    """
    stored_list: List[float] = []
    for _ in range(0, n):
        stored_list.append(await task_wait_random(max_delay))
    for i, _ in enumerate(stored_list):
        minimum = min(stored_list[i:])
        min_index = stored_list.index(minimum)
        temp = stored_list[i]
        stored_list[i] = minimum
        stored_list[min_index] = temp
    return stored_list
