#!/usr/bin/python3
"""Creating the LIFOCache class that does inherits from
the BaseCaching file"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Defining the LRUCache class """

    def __init__(self):
        """ Initializing the LRUCache class """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """ Assigning the item just to the present dictionary """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)

            self.queue.append(key)
            self.cache_data[key] = item

            if len(self.queue) > self.MAX_ITEMS:
                dellete = self.queue.pop(0)
                self.cache_data.pop(dellete)
                print('DISCARD: {}'.format(dellete))

    def get(self, key):
        """ Returning the actual value thats associated
        with the actuale given key """
        if self.cache_data.get(key):
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key)
