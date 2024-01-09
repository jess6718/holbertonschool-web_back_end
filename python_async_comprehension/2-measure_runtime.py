#!/usr/bin/env python3
"""Coroutine measure_runtime that will execute async_comprehension\
    4 times in parallel using asyncio.gather"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine measure the total runtime and return it"""
    start_at = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_at = time.time()
    total_time = end_at - start_at
    return total_time
