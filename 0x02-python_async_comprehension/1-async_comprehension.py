#!/usr/bin/env python3
"""
Collects 10 random numbers using an async comprehension over async_generator
"""
import asyncio
from typing import List

async_generator =  __import__('async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator
    and returns the list of these numbers.
    """
    return [number async for number in async_generator()]
