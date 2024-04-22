#!/usr/bin/env python3
"""task2
"""
import asyncio
import time


wait_n = __import__('2-measure_runtime').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure an approximate elapsed time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start_time) / n
