#!/usr/bin/env python3
"""
a coroutine called async_generator
that takes no arguments
"""
import random
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    a coroutine called async_generator
    that takes no arguments
    """
    for _ in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
