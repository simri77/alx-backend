#!/usr/bin/env python3
"""
Module 4-mru_cache
"""
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    A class used to represent MRUCache

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
        self.cache_data = OrderedDict()

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
        try:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        except KeyError:
            return

    def put(self, key, item):
        """
        Add an item in the cache using MRUCache eviction techniques

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
            try:
                self.cache_data.pop(key)
            except KeyError:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    last = self.cache_data.popitem()
                    print(f"DISCARD: {last[0]}")
            self.cache_data[key] = item
