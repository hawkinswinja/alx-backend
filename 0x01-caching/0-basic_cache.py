#!/usr/bin/env python3
"""0-basic_cache module that implements the BasicCache"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """implementation of basic cache"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """add data to the cache variable"""
        if key:
            if item:
                self.cache_data[key] = item

    def get(self, key):
        """returns a cache value of the data"""
        val = self.cache_data.get(key)
        return val
