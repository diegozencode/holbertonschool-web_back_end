#!/usr/bin/env python3
"""
Simple helper function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Range of indexes
    Parameters
    ------------
    page: int
        page number
    page_size: int
        size of the page
    Returns
    --------
    tuple
        The start and end indexes
    """
    start: int
    end: int

    end = page * page_size

    if page == 1:
        start = 0
    else:
        start = end - page_size

    return (start, end)
