import csv
from typing import List


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
