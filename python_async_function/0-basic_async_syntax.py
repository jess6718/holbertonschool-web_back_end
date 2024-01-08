#!/usr/bin/env python3
"""Asynchronous coroutine waits and return"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """await random delay"""
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
