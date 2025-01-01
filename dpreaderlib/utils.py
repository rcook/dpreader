from typing import Any
import itertools


def indices(start: int = 0, count: int | None = None) -> itertools.count | range:
    if count is None:
        return itertools.count(start)
    else:
        return range(start, start + count)
