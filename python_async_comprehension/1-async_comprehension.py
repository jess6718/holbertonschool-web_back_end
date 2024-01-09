#!/usr/bin/env python3
"""Coroutine async_comprehension that takes no arguments"""
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """the coroutine collect 10 random numbers return the list of numbers"""
    dataset = [data async for data in async_generator()]
    return dataset
