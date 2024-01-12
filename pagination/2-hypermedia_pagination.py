#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """
    Input two Int arguments
    return a tuple containing a start index and an end index
    """
    start = int(page_size * (page - 1))  # start index in the page
    end = int(page * page_size)  # end index in the page
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return the appropriate page of the dataset
        """
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        find_indexes = index_range(page, page_size)
        start_idx = find_indexes[0]
        end_idx = find_indexes[1]
        data = self.dataset()
        if page * page_size > len(data):  # out of range return empty list
            return []

        page_list = []
        i = start_idx

        for i in range(start_idx, end_idx):  # otherwise populate list
            page_list.append(data[i])
        return page_list

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing page_size, page, data, next_page,
        prev_page, total_pages
        """
        data_list = self.dataset()
        return_list = self.get_page(page, page_size)
        total_page = math.ceil(len(data_list) / page_size)
        next_page = page + 1
        if next_page > total_page:
            next_page = None  # next page is None if over the limit
        prev_page = page - 1
        if prev_page < 1:
            prev_page = None  # pre page is None if below 1
        return {
            "page_size": page_size,
            "page": page,
            "data": return_list,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_page
        }
