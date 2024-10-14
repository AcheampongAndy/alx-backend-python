#!/usr/bin/env python3
"""
    Waits for a random delay between 0 and max_delay seconds
    and returns the delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10)-> float:
    """
    Args:
        max_delay (int): Maximum value for the random
        delay in seconds. Defaults to 10.

    Returns:
        float: The amount of time the coroutine waits.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
