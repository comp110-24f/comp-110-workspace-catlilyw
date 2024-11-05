"""Creating a new river!"""

__author__ = "730655044"

from exercises.ex07.river import River

my_river: River = River(10, 2)

print(my_river.view_river())

print(my_river.one_river_week())
