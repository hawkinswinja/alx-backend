#!/usr/bin/env python3
"""1-fifo_cache module that implements the FIFOCache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """implementation of basic cache"""
    def __init__(self):
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """add data to the cache variable"""
        if key:
            if item:
                self.cache_data[key] = item
                if key in self.key_order:
                    self.key_order.remove(key)
                self.key_order.append(key)
                if len(self.key_order) > self.MAX_ITEMS:
                    new = self.key_order[-2]
                    del self.cache_data[new]
                    print('DISCARD:', new)
                    self.key_order.remove(new)

    def get(self, key):
        """returns a cache value of the data"""
        val = self.cache_data.get(key)
        return val
