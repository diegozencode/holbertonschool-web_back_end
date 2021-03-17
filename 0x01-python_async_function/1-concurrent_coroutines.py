#!/usr/bin/env python3
"""
execute multiple coroutines at the same time
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return the delay values
    Parameters
    ----------
    max_delay: int
        waiting time
    n: int
        number of times that wait_random spawn
    Returns
    -------
    List[float]
        all the delays in ascending order
    """
    my_list = []
    sorted_delays = []

    for i in range(n):
        my_list.append(wait_random(max_delay))

    for future in asyncio.as_completed(my_list):
        res = await future
        sorted_delays.append(res)

    return sorted_delays
