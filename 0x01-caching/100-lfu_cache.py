#!/usr/bin/python3
""" Creating the LIFOCache class that does inherits
from the BaseCaching file """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Defining the LRUCache class  """

    def __init__(self):
        """ Initializing the LFUCache class """
        self.queue = []
        self.lfu = {}
        super().__init__()

    def put(self, key, item):
        """ Assigning the item just to the present dictionary """
        if key and item:
            if (len(self.queue) >= self.MAX_ITEMS and
                    not self.cache_data.get(key)):
                dellete = self.queue.pop(0)
                self.lfu.pop(dellete)
                self.cache_data.pop(dellete)
                print('DISCARD: {}'.format(dellete))

            if self.cache_data.get(key):
                self.queue.remove(key)
                self.lfu[key] += 1

            else:
                self.lfu[key] = 0

            insert_the_index = 0

            while (insert_the_index < len(self.queue) and
                   not self.lfu[self.queue[insert_the_index]]):
                insert_the_index += 1

            self.queue.insert(insert_the_index, key)
            self.cache_data[key] = item

    def get(self, key):
        """ Returning the actual value thats associated
        with the actuale given key """
        if self.cache_data.get(key):
            self.lfu[key] += 1

            if self.queue.index(key) + 1 != len(self.queue):
                while (self.queue.index(key) + 1 < len(self.queue) and
                       self.lfu[key] >=
                       self.lfu[self.queue[self.queue.index(key) + 1]]):
                    self.queue.insert(self.queue.index(key) + 1,
                                      self.queue.pop(self.queue.index(key)))
        return self.cache_data.get(key)
