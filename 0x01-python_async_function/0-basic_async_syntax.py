#!/usr/bin/env python3
"""
The basic of asynchronous coroutine
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay and returns it
    Parameters
    ----------
    max_delay : int
        waiting time
    Returns
    -------
    float
        the delay time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
