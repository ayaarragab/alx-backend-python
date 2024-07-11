#!/usr/bin/env python3
"""
a coroutine called async_generator
that takes no arguments
"""
import random
from asyncio import sleep
from typing import AsyncIterator


async def async_generator() -> AsyncIterator[float]:
    """
    a coroutine called async_generator
    that takes no arguments
    """
    for i in range(0, 10):
        await sleep(1)
        yield random.uniform(0, 11)
