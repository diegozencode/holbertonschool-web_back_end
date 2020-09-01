#!/usr/bin/env python3
"""
Writing string to Redis
"""


import uuid
import redis
from typing import Union


class Cache:
    """store instance of redis
    """
    def __init__(self):
        """initialization
        """
        # store instance of redis client
        self._redis = redis.Redis()
        # flush the instance with 'flushdb'
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store the input
        """
        # generate key
        key = str(uuid.uuid4())
        # store
        self._redis.hmset(key, data)
        # return key
        return key
