#!/usr/bin/env python3
"""An asynchronous coroutine wait_n"""
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """List of all delays ascendingly"""
    result_list = [await wait_random(max_delay) for _ in range(n)]
    for i in range(len(result_list)):
        swapped = False
        for j in range(len(result_list) - i - 1):
            if result_list[j] > result_list[j + 1]:
                result_list[j], result_list[j + 1] =\
                        result_list[j + 1], result_list[j]
                swapped = True

        if not swapped:
            break  # If no swaps occur, list is already sorted, can break
    return result_list
