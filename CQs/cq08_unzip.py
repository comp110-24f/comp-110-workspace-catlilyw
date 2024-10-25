"""Splitting a dictionary into two lists"""

__author__ = "730655044"


def get_keys(dict1: dict[str, int]) -> list[str]:
    """getting all the keys from an input dict"""
    rlist: list[str] = []
    for key in dict1:
        rlist.append(key)
    return rlist
