#!/usr/bin/env python3
"""CountedIterator - Keeping Track of Iteration mandatory"""

class CountedIterator:
    """class that encapsulates an iterator and counts the number of elements iterated through"""
    def __init__(self, iterable):
        """initializes a CountedIterator with an iterable object"""
        self._iter = iter(iterable)
        self._count = 0

    def __iter__(self):
        """return the iterator object itself"""
        return self

    def __next__(self):
        """returns the next element of the iterator and increment the counter"""
        item = next(self._iter)
        self._count += 1
        return item

    def get_count(self):
        """returns the number of elements consumed via `__next__`"""
        return self._count

