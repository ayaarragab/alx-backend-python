#!/usr/bin/env python3
"""
a measure_runtime coroutine that will execute
async_comprehension four times
in parallel using asyncio.gather.
measure_runtime should measure the total runtime
and return it.
"""
import time
import asyncio
async_c = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a measure_runtime coroutine that will execute
    async_comprehension four times
    in parallel using asyncio.gather.
    measure_runtime should measure the total runtime
    and return it.
    """
    start: float = time.time()
    await asyncio.gather(async_c(), async_c(), async_c(), async_c())
    end: float = time.time()
    return end - start
