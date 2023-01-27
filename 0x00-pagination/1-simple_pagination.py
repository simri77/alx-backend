#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Tuple


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

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        return a tuple of size
        two containing a start index
        and an end index corresponding
        to the range of indexes to return
        in a list for those particular pagination parameters
        """
        end = page * page_size
        start = end - page_size
        return(start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 integer arguments and returns requested page from the dataset
        Args:
            page (int): required page number. must be a positive integer
            page_size (int): number of records per page. must be a +ve integer
        Return:
            list of lists containing required data from the dataset
        """
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        result = self.index_range(page, page_size)
        data = self.dataset()
        if len(data) < result[0]:
            return []
        return data[result[0]: result[1]]
