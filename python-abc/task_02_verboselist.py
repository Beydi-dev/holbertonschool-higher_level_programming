#!/usr/bin/python3
"""creating VerboseList class"""


class VerboseList(list):
    """VerboseList class and methods"""
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items."
              .format(", ".join(map(str, item))))

    def remove(self, item):
        print("Removed [{}] from the list."
              .format(item))  # printing the object before deletion
        super().remove(item)

    def pop(self, index=-1):
        valeur = self[index]  # recovering the object before popping it
        print(f"Popped {[valeur]} from the list.")
        return super().pop(index)
