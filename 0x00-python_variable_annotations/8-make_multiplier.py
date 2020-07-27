#!/usr/bin/env python3
"""
Complex types - functions
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function callable
    """
    return lambda a: a * multiplier
