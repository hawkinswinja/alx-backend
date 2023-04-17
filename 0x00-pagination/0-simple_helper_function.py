#!/usr/bin/env python3
"""
helper function to get page indexes
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """return a tuple of size two containing a start and an end index"""
    start = 0
    end = page_size
    if page > 1:
        start = (page - 1) * page_size
        end = page * page_size
    return (start, end)
