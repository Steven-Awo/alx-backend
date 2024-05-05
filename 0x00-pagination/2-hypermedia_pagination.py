#!/usr/bin/env python3
''' Description: Implement a get_hyper method that takes the same arguments
                 (and defaults) as get_page and returns a dictionary containing
                 the following key-value pairs
'''

import csv

from math import ceil

from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """This server class helps to paginate a particular
    database of the popular baby's names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' Initializing every instance needed. '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """The cached's dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                readder = csv.reader(f)
                data_of_set = [roww for roww in readder]
            self.__dataset = data_of_set[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Prints the output page of the dataset. '''
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0

        indiccess = index_range(page, page_size)
        startt = indiccess[0]
        endd = indiccess[1]

        try:
            return self.dataset()[startt:endd]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        ''' Returning the dict of the pagination's data. Dict's key/value
        pairs that consist of all the following:
                page_size - the length of the returned dataset page
                page - the current page number
                data - the dataset page (equivalent to return
                from previous task)
                next_page: number of the next page, None if no next page
                prev_page: number of the previous page, None
                if no previous page
                total_pages: the total number of pages in the
                dataset as an integer '''
        page_of_data = self.get_page(page, page_size)
        total_of_data = len(self.dataset())
        total_of_pages = ceil(total_of_data / page_size)

        return {
            'page_size': len(page_of_data),
            'page': page,
            'data': page_of_data,
            'next_page': page + 1 if page < total_of_pages else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_pages': total_of_pages
        }
