#!/usr/bin/env python3
"""
Async generator
"""


import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Coroutine that will loop 10 times and wait 1 sec
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
