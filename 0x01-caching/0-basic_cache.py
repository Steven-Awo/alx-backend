#!/usr/bin/python3
"""Creating a BasicCache class that does inherits from the
BaseCaching"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defining the BasicCache class """

    def put(self, key, item):
        """ Assigning the item just to the dictionary """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Returning the actaul value thats associated with
        the actual given key """
        return self.cache_data.get(key)
