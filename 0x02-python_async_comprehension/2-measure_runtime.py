#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure runtime of async comprehension 4 times """

    start_time = time.perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = time.perf_counter()
    total_dur = end_time - start_time
    return total_dur
