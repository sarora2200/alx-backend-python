#!/usr/bin/env python3
"""task 1"""
import asyncio
from typing import list

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """return the list of all the delays float values"""
    wait_times = await asynico.gather(
            *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
