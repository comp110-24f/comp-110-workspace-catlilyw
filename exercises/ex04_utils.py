"""Exercise for list utility functions!"""

__author__ = "730655044"


def all(int_list: list[int], checker: int) -> bool:
    """Checks to see if all of the ints in a list are the same"""
    if len(int_list) == 0:  # get rid of empty lists before entering loop
        return False
    idx: int = 0
    while idx < len(int_list):
        if int_list[idx] != checker:  # shouldn't be true if list is empty
            idx += 1
            return False
        else:
            idx += 1  # needed to continue in the loop if if statement is false
    return True


print(all([1, 1, 1], 1))


def max(input: list[int]) -> int:
    """Checks for the largest value in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    highest: int = input[idx]
    while idx < len(input):
        if input[idx] > highest:  # like the highest card example!
            highest = input[idx]
            idx += 1
        else:
            idx += 1
    return highest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if every item is the same between 2 lists"""
    idx: int = 0
    while idx < len(list1) or idx < len(list2):
        if (
            len(list1) != len(list2) or list1[idx] != list2[idx]
        ):  # must be the same value at the same idx
            idx += 1
            return False
        else:
            idx += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    idx: int = 0
    while idx < len(
        list2
    ):  # len of list2 is the only one that matters for this conditional
        list1.append(list2[idx])  # must append only one item to a list at a time
        idx += 1
