#!/usr/bin/env python3
'''Description: Implementing a method named get_page that takes
                two integer arguments page with default value 1
                and page_size with default value 10.
'''

import csv

import math

from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """This server class helps to paginate a particular
    database of the popular baby's names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' Initializing every instance. '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """The cached's dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                readder = csv.reader(f)
                datasset = [roww for roww in readder]
            self.__dataset = datasset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        ''' Prints the output page of the dataset. '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indicces = index_range(page, page_size)
        starrt = indicces[0]
        endd = indicces[1]

        try:
            return self.dataset()[starrt:endd]
        except IndexError:
            return []
