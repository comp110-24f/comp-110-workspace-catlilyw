from lessons.qz02.qz02 import diclength


def test_diclength():
    """Use case for diclength"""
    fruit: list[str] = ["apples", "oranges", "strawberries"]
    assert diclength(fruit) == {"apples": 6, "oranges": 7, "strawberries": 12}
