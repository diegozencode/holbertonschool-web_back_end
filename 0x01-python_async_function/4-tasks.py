#!/usr/bin/env python3
"""
execute multiple coroutines at the same time
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the delay values
    Parameters
    ----------
    n: int
        number of times that wait_random spawn
    max_delay: int
        waiting time
    Returns
    -------
    List[float]
        all the delays in ascending order
    """
    my_list = []
    sorted_delays = []

    for i in range(n):
        my_list.append(task_wait_random(max_delay))

    for future in asyncio.as_completed(my_list):
        res = await future
        sorted_delays.append(res)

    return sorted_delays
