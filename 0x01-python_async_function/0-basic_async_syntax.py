#!/usr/bin/env python3

import asyncio
import random

async def wait_random(max_delay: int = 10)-> float:
    """
    Waits for a random delay between 0 and max_delay seconds
    and returns the delay.

    Args:
        max_delay (int): Maximum value for the random
        delay in seconds. Defaults to 10.

    Returns:
        float: The amount of time the coroutine waits.
    """
    # Generate a random float between 0 and max_delay (inclusive)
    delay = random.uniform(0, max_delay)

    # Pause execution for the duration of the random delay
    await asyncio.sleep(delay)

    # Return the random delay after waiting
    return delay
