#!/usr/bin/env python3
"""100-lfu_cache module that implements the LFUCache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """implementation of basic cache"""
    def __init__(self):
        super().__init__()
        self.key_nb = {}
        self.key_order = []

    def put(self, key, item):
        """add data to the cache variable and discard extra cache"""
        if key:
            if item:
                if len(self.key_order) >= self.MAX_ITEMS:
                    if not self.cache_data.get(key):
                        least = min(self.key_nb.values())
                        l_keys = list(filter(lambda x: self.key_nb[x] == least,
                                             self.key_nb))
                        if len(l_keys) < 2:
                            d_key = l_keys[0]
                        else:
                            d_key = len(self.key_order) - 1
                            for i in l_keys:
                                if self.key_order.index(i) < d_key:
                                    d_key = self.key_order.index(i)
                            d_key = self.key_order[d_key]
                        print('DISCARD:', d_key)
                        self.key_order.remove(d_key)
                        del self.key_nb[d_key]
                        del self.cache_data[d_key]
            self.cache_data[key] = item
            if key in self.key_order:
                self.key_order.remove(key)
                self.key_nb[key] += 1
            else:
                self.key_nb[key] = 1
            self.key_order.append(key)

    def get(self, key):
        """returns a cache value of the data"""
        val = self.cache_data.get(key)
        if val:
            self.key_order.remove(key)
            self.key_order.append(key)
            self.key_nb[key] += 1
        return val
