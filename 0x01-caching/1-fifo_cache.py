#!/usr/bin/python3
"""module"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """fifo cache class"""
    def __init__(self):
        """initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put caching"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(False)
                print("DISCARD: {}".format(first_key), end="\n")
            self.cache_data[key] = item

    def get(self, key):
        """get caching"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
