#!/usr/bin/env python3
"""
    Measure the total execution time for wait_n(n, max_delay) and
    return the average time per coroutine.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n (int): Number of times to spawn wait_random in wait_n.
        max_delay (int): Maximum delay value for wait_random.

    Returns:
        float: The average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
