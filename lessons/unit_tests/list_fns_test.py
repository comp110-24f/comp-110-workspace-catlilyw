"""Testing the list_fns"""

from lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first

"""Use cases!!!!"""


def test_get() -> None:
    """Test that get_first returns first elem"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_first(fruits) == "apples"


def test_remove() -> None:
    """Test that remove_first returns None"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert remove_first(fruits) is None


def test_remove_behavior() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    remove_first(fruits)
    assert fruits == ["oranges", "bananas"]


def test_get_and_return() -> None:
    """Test that get_and_remove_first returns first elem"""
    fruits: list[str] = ["apples", "oranges", "bananas"]
    assert get_and_remove_first(fruits) == "apples"


def test_get_and_return_behavior() -> None:
    fruits: list[str] = ["apples", "oranges", "bananas"]
    get_and_remove_first(fruits)
    assert fruits == ["oranges", "bananas"]


"""Edge cases!!!"""


def test_get_first_edge_case() -> None:
    """Test that get first works with empty list"""  # fails, modify function
    assert get_first([""]) == ""
