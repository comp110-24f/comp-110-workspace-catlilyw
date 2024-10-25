"""Finding the max of a list"""

__author__ = "730655044"


def find_and_remove_max(test_list: list[int]) -> int:
    """Finding the max of a list"""
    if len(test_list) == 0:  # need a conditional to code the -1 return
        return -1
    max_value: int = 0  # start at 0 otherwise it gets weird
    index: int = 0  # for while loop
    for idx in range(0, len(test_list)):
        if test_list[idx] > max_value:  # finding the highest card
            max_value = test_list[idx]
    while index < len(test_list):
        if test_list[index] == max_value:
            test_list.pop(index)  # pop the index not the value
        else:
            index += 1
    # print(test_list) to check!
    return max_value
