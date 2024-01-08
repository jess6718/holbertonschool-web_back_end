#!/usr/bin/env python3
"""Basic annotated function"""
from typing import Callable


def make_multiplier(multi: float) -> Callable[[float], float]:
    """Function takes a float and returns a function"""
    def call_func(x: float) -> float:
        return x * multi
    return call_func
