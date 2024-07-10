#!/usr/bin/env python3
"""
Write a function (do not create an async function,
use the regular function syntax to do this)
task_wait_random that takes an integer max_delay
and returns a asyncio.Task
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay):
    """
    Write a function (do not create an async function,
    use the regular function syntax to do this)
    task_wait_random that takes an integer max_delay
    and returns a asyncio.Task
    """
    return asyncio.Task(coro=wait_random(max_delay))
