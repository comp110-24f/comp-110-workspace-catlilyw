"""Challenge Question with while loops!"""

__author__ = "730655044"


def num_instances(phrase: str, search_char: str) -> int:
    """find out the number of times a letter appears in a phrase"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1  # put count in the same function block as index
            index += 1
        else:
            index += 1
    return count
