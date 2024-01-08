#!/usr/bin/env python3
"""Basic type-annotation"""
from typing import List
from typing import Tuple
from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuple containing the element and its length"""
    return [(i, len(i)) for i in lst]
