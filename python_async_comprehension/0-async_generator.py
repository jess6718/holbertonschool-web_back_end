#!/usr/bin/env python3
"""Coroutine async_generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine loop 10 times and wait 1 sec, yield random out a number"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
