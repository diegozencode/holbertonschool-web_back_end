#!/usr/bin/env python3
"""
execute multiple coroutines at the same time
"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(max_delay: int, n: int):
    """return the delay values"""
    my_list = []
    for i in range(n):
        my_list.append(await wait_random(max_delay))

    return my_list
