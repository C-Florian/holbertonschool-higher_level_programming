#!/usr/bin/env python3
"""Extending the Python List with Notifications"""

class VerboseList(list):
    """class that inherits from the built-in list"""

    def append(self, item):
        """define a method that item to the list and print a message"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """define a method that extend the list and print a message"""
        count = len(list(iterable))
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """ define a method that print a message before removing the item"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """define a method that print a message before popping item from the list"""
        if index is None:
            item = super().pop()
        else:
            item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item

