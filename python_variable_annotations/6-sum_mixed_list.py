#!/usr/bin/env python3
"""Basic annotated function"""
from typing import List
from typing import Union

Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """function takes a mixed list and return sum as a float"""
    return sum(mxd_lst)
