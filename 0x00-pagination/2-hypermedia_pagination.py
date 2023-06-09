#!/usr/bin/env python3
"""
helper function to get page indexes
"""
import csv
import math
from typing import Tuple, List, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, int]:
        """return dictionary statusof paginated data"""
        data = self.get_page(page, page_size)
        next_page = None
        prev_page = None
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if len(data) == 0:
            page_size = 0
        if page < total_pages:
            next_page = page + 1
        if page > 1:
            prev_page = page - 1

        return {'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
