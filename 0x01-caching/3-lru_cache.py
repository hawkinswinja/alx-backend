#!/usr/bin/env python3
"""3-lru_cache module that implements the LRUCache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
                    new = self.key_order[0]
                    del self.cache_data[new]
                    print('DISCARD:', new)
                    self.key_order.remove(new)

    def get(self, key):
        """returns a cache value of the data"""
        val = self.cache_data.get(key)
        if val:
            self.key_order.remove(key)
            self.key_order.append(key)
        return val
