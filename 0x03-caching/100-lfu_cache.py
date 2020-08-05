#!/usr/bin/env python3
"""
LFU Caching
"""


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Least Frequently used
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.cache_time = {}
        self.cache_access = {}
        self.access_history = 0

    def put(self, key: str, item: str):
        """Add an item in the cache
        """
        if key is None or item is None:
            return

        self.cache_time[key] = self.access_history
        self.cache_data[key] = item
        if key in self.cache_access:
            self.cache_access[key] += 1
        else:
            self.cache_access[key] = 1
        self.access_history += 1

        if len(self.cache_data) <= BaseCaching.MAX_ITEMS:
            return

        my_list = [
                k for k, v in sorted(
                    self.cache_access.items(),
                    key=lambda p: p[1]
                    )]
        min_access = self.cache_access[my_list[1]]
        listItem = self.getKeysByValue(self.cache_access, min_access)

        if len(listItem) > 1:
            my_new_dict = {}

            for i in listItem:
                my_new_dict[i] = self.cache_time[i]

            old_key = min(
                my_new_dict.keys(),
                key=lambda k: my_new_dict[k]
            )
            self.cache_data.pop(old_key)
            self.cache_time.pop(old_key)
            self.cache_access.pop(old_key)
            print("DISCARD: " + str(old_key))
        else:
            self.cache_data.pop(my_list[1])
            self.cache_time.pop(my_list[1])
            self.cache_access.pop(my_list[1])
            print("DISCARD: " + str(my_list[1]))

    def get(self, key: str):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.cache_time[key] = self.access_history
        self.cache_access[key] += 1
        self.access_history += 1
        return self.cache_data[key]

    def getKeysByValue(self, elements, value):
        """get keys
        """
        listKeys = list()
        listItems = elements.items()

        for item in listItems:
            if item[1] == value:
                listKeys.append(item[0])

        return listKeys
