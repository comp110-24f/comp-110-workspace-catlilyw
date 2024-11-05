"""File to define Bear class."""

__author__ = "730655044"


class Bear:
    """New class/type of Bear!"""

    age: int
    hunger_score: int

    def __init__(self):
        """Initializing the bear."""
        self.age = 0  # initial values should be 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Age and hunger of the bear after one day."""
        self.age += 1
        self.hunger_score -= 1  # bear gets hungrier when it can't eat
        return None

    def eat(self, num_fish: int):
        """Eating the fish and updating the bear's hunger."""
        self.hunger_score += num_fish
