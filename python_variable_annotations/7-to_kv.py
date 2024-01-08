#!/usr/bin/env python3
"""Basic annotated function"""
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function takes string return as a tuple"""
    first: str = k
    second: float = v ** 2
    result = (first, second)
    return result
