"""Utils test for ex05"""

__author__ = "730655044"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index

"""only_evens tests"""


def test_even_return() -> None:
    """Return test for only_even"""
    input: list[int] = [1, 2, 3, 4, 5, 6]
    assert only_evens(input) == [2, 4, 6]


def test_even_mutate() -> None:
    """Mutation test for only_even"""
    input: list[int] = [1, 2, 3, 4, 5, 6]
    only_evens(input)
    assert input == [1, 2, 3, 4, 5, 6]


def test_even_edge() -> None:
    """Tests if only_evens returns anything with an empty input list"""
    input: list[int] = []
    assert only_evens(input) == []


"""sub tests"""


def test_sub_return() -> None:
    """Return test for sub"""
    input: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(input, 2, 4) == [3, 4]


def test_sub_mutate() -> None:
    """Mutation test for sub"""
    input: list[int] = [1, 2, 3, 4, 5, 6]
    sub(input, 2, 4)
    assert input == [1, 2, 3, 4, 5, 6]


def test_sub_edge() -> None:
    """Tests if sub starts at the correct index with a negative start_idx value"""
    input: list[int] = [1, 2, 3, 4, 5, 6]
    assert sub(input, -1, 3) == [1, 2, 3]


"""add_at_integer tests"""


def test_add_return() -> None:
    """Return test for add_at_index"""
    input: list[int] = [1, 2, 4, 5, 6]
    assert add_at_index(input, 3, 2) is None


def test_add_mutate() -> None:
    """Mutation test for add_at_index"""
    input: list[int] = [1, 2, 4]
    add_at_index(input, 3, 2)
    assert input == [1, 2, 3, 4]


def test_add_edge() -> None:
    """Tests if function works with only one element in the initial list"""
    input: list[int] = [1]
    add_at_index(input, 3, 0)
    assert input == [3, 1]
