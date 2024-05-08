#!/usr/bin/python3
"""Creating the LIFOCache class that does inherits
from the BaseCaching file"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Defining the LIFOCache class """

    def __init__(self):
        """ Initializing the LIFOCache class """
        self.stack = []
        super().__init__()

    def put(self, key, item):
        """ Assigning the item just to the dicti """
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)

            while len(self.stack) >= self.MAX_ITEMS:
                dellete = self.stack.pop()
                self.cache_data.pop(dellete)
                print('DISCARD: {}'.format(dellete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returning the actual value thats associated with
        actual the given key """
        return self.cache_data.get(key)
