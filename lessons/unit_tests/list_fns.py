"""Funtions to try unit testing"""


def get_first(list1: list[str]) -> str:
    """Returns first str"""
    return list1[0]


def remove_first(list2: list[str]) -> None:
    """Mutates og list->removes first str"""
    list2.pop(0)
    # print(list2)


def get_and_remove_first(list3: list[str]) -> str:
    """Returns first str and removes first str"""
    first: str = list3[0]  # need local variable so don't lose og value of first str
    list3.pop(0)
    # print(list3)
    return first
