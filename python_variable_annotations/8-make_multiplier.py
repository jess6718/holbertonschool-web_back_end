#!/usr/bin/env python3
"""Basic annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function takes a float and returns a function"""
    def call_func(x: float) -> float:
        return x * multiplier
    return call_func
