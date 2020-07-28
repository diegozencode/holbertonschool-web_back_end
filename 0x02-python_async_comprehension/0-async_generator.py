#!/usr/bin/env python3
"""
Async generator
"""


import asyncio
import random


async def async_generator():
    """Coroutine that will loop 10 times and wait 1 sec
    """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
