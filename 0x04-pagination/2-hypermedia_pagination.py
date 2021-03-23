#!/usr/bin/env python3
"""
Hypermedia pagination
"""


import csv
import math
from typing import List, Dict


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Dataset page
        Parameters
        ------------
        page: int
            page number, has to be an int and greater than 0
        page_size: int
            size of the page, has to be an int and greater than 0
        Returns
        --------
        list
            page of the dataset, list of rows, empty list if out of range
        """
        assert(type(page) == int and type(page_size) == int)
        assert (page > 0 and page_size > 0), "Testing"

        start: int = index_range(page, page_size)[0]
        end: int = index_range(page, page_size)[1]
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Dataset dictionary hypermedia
        Parameters
        ------------
        page: int
            page number, has to be an int and greater than 0
        page_size: int
            size of the page, has to be an int and greater than 0
        Returns
        --------
        dictionary
            dataset
        """
        dataset: List[List] = self.get_page(page, page_size)
        total: int = math.ceil(len(self.dataset()) / page_size)
        next_page = None
        prev_page = None

        if page < total:
            next_page = page + 1

        if page > 1:
            prev_page = page - 1

        data = {
            'page_size': len(dataset),
            'page': page,
            'data': dataset,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total
        }

        return data
