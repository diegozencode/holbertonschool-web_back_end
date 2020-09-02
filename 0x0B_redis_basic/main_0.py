#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache

cache = Cache()

test = cache.store(b"first")
cache.store(b"second")
cache.store(b"third")
print(test)