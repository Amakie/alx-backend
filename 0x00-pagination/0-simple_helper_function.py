#!/usr/bin/env python3
""" function that takes two integer arguments page and page_size"""

from typing import tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """return a tuple of the start and end pages"""
    return (((page-1) * page_size), (page * page_size))
