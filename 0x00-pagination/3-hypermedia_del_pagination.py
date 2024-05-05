#!/usr/bin/env python3
"""
Description: The goal here is that if between two queries, certain
            rows are removed from the dataset, the user does not
            miss items from dataset when changing page.Implement
            a get_hyper_index method with two integer arguments:
            index with a None default value and page_size with
            default value of 10.
"""

import csv

import math

from typing import List, Dict


class Server:
    """This server class helps to paginate a particular
    database of the popular baby's names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        ''' Initialize instance. '''
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """The cached's dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                readder = csv.reader(f)
                data_of_set = [roww for roww in readder]
            self.__dataset = data_of_set[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """A dataset's indexed by just sorting the position,
        starting at 0
        """
        if self.__indexed_dataset is None:
            data_set = self.dataset()
            truncated_dataset = data_set[:1000]
            self.__indexed_dataset = {
                a: data_set[a] for a in range(len(data_set))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        ''' Returning the dict of the pagination data.
            Dict key/value pairs consist of the following:
              index - the starting index  for or of the page
              next_index - the starting index of just the next
              page's page_size
              page_size - the total number of items thats on
              the page
              data - the data thats in the actual page itself '''
        assert 0 <= index < len(self.dataset())

        indexed_of_dataset = self.indexed_dataset()
        indexed_of_page = {}

        a = index
        while (len(indexed_of_page) < page_size and a < len(self.dataset())):
            if a in indexed_of_dataset:
                indexed_of_page[a] = indexed_of_dataset[a]
            a += 1

        pagee = list(indexed_of_page.values())
        page_of_indices = indexed_of_page.keys()

        return {
            'index': index,
            'next_index': max(page_of_indices) + 1,
            'page_size': len(pagee),
            'data': pagee
        }
