"""File to define River class."""

__author__ = "730655044"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """New class/type of River!"""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checking the ages of the animals."""
        new_bears: list[Bear] = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears  # updated self.bears without changing it during the loop
        new_fish: list[Fish] = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish
        return None

    def remove_fish(self, amount: int):
        """Removing fish from the front of the list."""
        idx: int = 0
        count: int = 0  # keeping track of the amount
        while count < amount:  # removing the fish while counting
            self.fish.pop(idx)
            count += 1

    def bears_eating(self):
        """Bears eating fish and removing those fish."""
        for bear in self.bears:
            if len(self.fish) > 5:
                bear.eat(3)  # this needs to be above removing fish
                River.remove_fish(self, 3)
        return None

    def check_hunger(self):
        """Seeing if the bear has starved."""
        full_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                full_bears.append(bear)
        self.bears = full_bears
        return None

    def repopulate_fish(self):
        """Putting more fish in the river."""
        for idx in range(
            0, len(self.fish) - 1, 2
        ):  # length needs to be -1 so it doesn't add extra
            self.fish.append(
                Fish()
            )  # appending a new fish to the end of the list 4 times per pair of fish
            self.fish.append(Fish())
            self.fish.append(Fish())
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Putting more bears in the river."""
        for idx in range(0, len(self.bears), 2):
            self.bears.append(self.bears[idx])
        return None

    def view_river(self):
        """Visualizing the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week in life in the river."""
        River.one_river_day(self)  # calling it 7 separate times
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        return None
