#!/usr/bin/env python3

from 0-basic_async_syntax import wait_random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the list
    of all delays in ascending order without using sort().

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum value for the random delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    all_delays = [wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*all_delays)

    ordered_delays = []

    while delays:
        min_delay = min(delays)
        ordered_delays.append(min_delay)
        delays.remove(min_delay)

    return ordered_delays
