#!/usr/bin/python3
"""class CountedIterator"""


class CountedIterator:
    """defining all the methods"""
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count

    def __next__(self):
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterate")
