#!/usr/bin/env python3
"""
Complex types - mixed list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum a list of floats and integers
    """
    sum: float = 0
    for n in mxd_lst:
        sum = sum + n

    return sum
