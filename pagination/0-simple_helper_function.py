#!/usr/bin/env python3
"""Pagination"""


def index_range(page, page_size):
    """
    Input two Int arguments
    return a tuple containing a start index and an end index
    """
    start = int(page_size * (page - 1))  # start index in the page
    end = int(page * page_size)  # end index in the page
    return (start, end)
