#!/usr/bin/python3
"""module
"""
import csv
import math
from typing import List


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

    def index_range(self, page: int, page_size: int) -> tuple:
        """return a tuple of size two containing a
        start index and an end index corresponding
        to the range of indexes to return in a list for
        those particular pagination parameters."""
        start_idx = (page - 1) * page_size
        end_idx = page * page_size
        return start_idx, end_idx

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        start_idx, end_idx = self.index_range(page, page_size)
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """returns a dictionary containing the following key-value
        """
        assert type(page) is int and type(page_size) is int
        assert page > 0 and page_size > 0
        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)
        start_idx, end_idx = self.index_range(page, page_size)
        page_data = dataset[start_idx:end_idx]
        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
