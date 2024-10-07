"""Mutating functions."""

__author__ = "730655044"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # sets them equal, will have the same heap output
# since both list 1 and 2 are references to the same set of items.


def manual_append(list: list[int], int: int) -> None:
    """To add values to a list"""
    list.append(int)


def double(list2: list[int]) -> None:
    """Doubles all the items in a list"""
    idx: int = 0
    while idx < len(list2):  # idx should never be = to the length of the list
        list2[idx] = list2[idx] * 2  # the function to double every item
        idx += 1


double(list_2)
print(list_1)
print(list_2)
