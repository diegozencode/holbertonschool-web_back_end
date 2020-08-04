#!/usr/bin/env python3
"""
Fifo caching
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """First In First Out
    """

    def put(self, key: str, item: str):
        """ Add an item in the cache
        """
        if (key is not None and item is not None):
            self.cache_data[key] = item
            if len(self.cache_data) > self.MAX_ITEMS:
                my_list = list(self.cache_data)
                del self.cache_data[my_list[0]]
                print("DISCARD: " + str(my_list[0]))

    def get(self, key: str):
        """ Get an item by key
        """
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]
