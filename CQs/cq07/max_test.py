"""Testing the find_max file"""

__author__ = "730655044"

from CQs.cq07.find_max import find_and_remove_max


def test_find_and_remove_return() -> None:
    """Determine if the function gives the proper output"""
    input: list[int] = [1, 2, 3, 4]
    assert find_and_remove_max(input) == 4


def test_find_and_remove_behavior() -> None:
    """Determine if the function mutates the input correctly"""
    input: list[int] = [1, 2, 3, 4]
    find_and_remove_max(input)  # call it to run the mutation
    assert input == [1, 2, 3]  # mutated input


def test_edge_case_blank() -> None:
    """Determine if the function returns the proper value for a blank list"""
    input: list[int] = []  # empty list
    assert find_and_remove_max(input) == -1  # desired output
