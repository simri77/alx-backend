#!/usr/bin/env python3
"""
Module 2-lifo_cache.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A class used to represent LIFOCache

    Arguments
    ---------
    key: str
    key name of cache_data dictionary
    item: str
        value corresponding to a given key of cache_data dictionary
    Methods
    -------
    put(key, item)
        Add an item in the cache
    get(key)
        Get an item by key
    """
    def __init__(self):
        """ Initialize the class using the parent class __int__ method"""
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache using LIFO eviction techniques

        Parameters
        ----------
        key: str
          key name of cache_data dictionary
        item: str
            value corresponding to a given key of cache_data dictionary
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if key not in self.cache_data.keys():
                    last = self.cache_data.popitem()
                    print(f"DISCARD: {last[0]}")
                else:
                    self.cache_data.pop(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key

        Parameters
        ----------
        key: str
            key name of cache_data dictionar

        Returns
        -------
        str
          item corresponding to a given key or
          none if the key is none or does't exist
        """
        if key is None or key not in self.cache_data.keys():
            return
        return self.cache_data.get(key)
