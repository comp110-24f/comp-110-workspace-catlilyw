"""Utils for ex05"""

__author__ = "730655044"


def only_evens(test_list: list[int]) -> list[int]:
    """Returns a list of only the even integers in a list"""
    even_list: list[int] = []  # need an empty list to add to & to return
    for idx in range(0, len(test_list)):
        if test_list[idx] % 2 == 0:  # to result in even numbers
            even_list.append(test_list[idx])
    return even_list


def sub(test_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Returns a list between 2 indexes"""
    sub_list: list[int] = []
    if start_idx < 0:
        start_idx = 0  # so it's not out of range
    if end_idx > len(test_list):
        end_idx = len(test_list)  # only one = silly
    for idx in range(start_idx, end_idx):
        sub_list.append(test_list[idx])
    return sub_list


# def add_at_index(test_list: list[int], add_elem: int, add_idx: int) -> None:
#     """Add an integer to a list at a specific index"""
#     if add_idx < 0 or add_idx > len(test_list):
#         raise IndexError("Index is out of bounds for the input list")
#     end: list[int] = []
#     for idx in range(
#         add_idx, len(test_list)
#     ):  # every idx btw the add_idx and the end of the list
#         end.append(test_list[idx])  # adds the popped values to an empty list
#         # test_list.pop(idx)  # removing the elements at incorrect indeces
#     test_list.append(add_elem)  # adding the desired element to the shortened test
# list
#     test_list += end


def add_at_index(test_list: list[int], add_elem: int, add_idx: int) -> None:
    """Add an integer to a list at a specific index"""
    if add_idx < 0 or add_idx > len(test_list):
        raise IndexError("Index is out of bounds for the input list")
    test_list.append(add_elem)  # add elem to the end of the test list
    for idx in range(
        len(test_list) - 1, add_idx, -1
    ):  # needs to step backwards and move one step at a time
        test_list[idx] = test_list[idx - 1]  # the actual backwards movement
    test_list[add_idx] = add_elem  # add_elem is put at the correct idx


# low_list: list[int] = []
# high_list: list[int] = []
# for idx in range(0, add_idx):
#   low_list.append(test_list[idx])
# for idx in range(add_idx, len(test_list)):
#   high_list.append(test_list[idx])
# low_list.append(add_elem)
# test_list = low_list + high_list
