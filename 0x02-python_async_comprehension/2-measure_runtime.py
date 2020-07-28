#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""


import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure time
    """
    s: float = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                        async_comprehension(),
                        async_comprehension(),
                        async_comprehension())
    total_time: float = time.perf_counter() - s
    return total_time
