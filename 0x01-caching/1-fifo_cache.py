#!/usr/bin/python3
"""Creating the FIFOCache class that actally inherits from the BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ Defining the FIFOCache class to be used """

    def __init__(self):
        """ Initializing the FIFOCache class """
        self.queue = []
        super().__init__()

    def put(self, key, item):
        """ Assigning all the item to the very dictionary """
        if key and item:
            if self.cache_data.get(key):
                self.queue.remove(key)
            self.queue.append(key)
            self.cache_data[key] = item

            if len(self.queue) > self.MAX_ITEMS:
                deleete = self.queue.pop(0)
                self.cache_data.pop(deleete)
                print('DISCARD: {}'.format(deleete))

    def get(self, key):
        """ Outputing the values thats associated with all
        the actual given key """
        return self.cache_data.get(key)
