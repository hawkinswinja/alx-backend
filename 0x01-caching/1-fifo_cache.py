#!/usr/bin/env python3
"""1-fifo_cache module that implements the FIFOCache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """implementation of basic cache"""
    def __init__(self):
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """add data to the cache variable"""
        if key:
            if item:
                self.cache_data[key] = item
                if key not in self.key_order:
                    self.key_order.append(key)
                    a = self.key_order[0]
                if len(self.key_order) > self.MAX_ITEMS:
                    del self.cache_data[a]
                    print('DISCARD:', a)
                    self.key_order.remove(a)

    def get(self, key):
        """returns a cache value of the data"""
        val = self.cache_data.get(key)
        return val
