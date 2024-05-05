#!/usr/bin/env python3
"""This is a basic helper function"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returning a tuple thats of the size of two containing
    a starting index and then an ending index"""

    return (page * page_size - page_size, page * page_size)
