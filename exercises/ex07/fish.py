"""File to define Fish class."""

__author__ = "730655044"


class Fish:
    """New class/type of fish!"""

    age: int

    def __init__(self):
        """Initializing the fish."""
        self.age = 0
        return None

    def one_day(self):
        """Age of fish after one day."""
        self.age += 1
        return None
