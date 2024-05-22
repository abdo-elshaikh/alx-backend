#!/usr/bin/python3
"""module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Base cache class"""

    def put(self, key, item):
        """put caching"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get caching"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
