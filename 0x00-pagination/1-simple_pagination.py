#!/usr/bin/env python3

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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
    Use assert to verify that both arguments
    are integers greater than 0
    return the appropriate page of the dataset
    """

    assert type(page) is int and page > 0
    assert type(page_size) is int and page_size > 0

    result = self.index_range(page, page_size)
    data = self.dataset()
    if len(data) < result[0]:
        return []
    return data[result[0]: result[1]]
