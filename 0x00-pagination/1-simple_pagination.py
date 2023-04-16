#!/usr/bin/env python3
"""
helper function to get page indexes
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start and an end index"""
    start = 0
    end = page_size
    if page > 1:
        start = (page - 1) * page_size
        end = page * page_size
    return (start, end)

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
        """fetch data within a defined range"""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        ranges = index_range(page, page_size)
        try:
            return self.dataset()[ranges[0]: ranges[1]]
        except IndexError:
            return []
