#!/usr/bin/env python3
"""Basic caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class inheriting from parent class BaseCaching"""

    def __init__(self):
        """initializing self"""
        super().__init__()


    def put(self, key, item):
        """function that adds item in cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key"""
        return self.cache_data.get(key, None)
