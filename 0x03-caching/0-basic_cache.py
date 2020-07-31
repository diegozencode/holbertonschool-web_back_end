#!/usr/bin/env python3
"""
Basic dictionary
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache dictionary
    """

    def put(self, key: str, item: str):
        """ Add an item in the cache
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item

    def get(self, key: str):
        """ Get an item by key
        """
        if (key in self.cache_data):
            return self.cache_data[key]
        return None
