"""Testing out lists!"""

grocery_list: list[str] = ["bananas", "milk", "bread"]  # the list!

grocery_list.append(
    "bananas"
)  # would add "bananas to the end; still functions with duplicate items"

grocery_list.pop(1)  # would remove "milk"

grocery_list[1] = "eggs"  # REPLACES "bread", does not add and shift the rest

len(grocery_list)  # amount of items in the list (would print 3)

grocery_list[1]  # would print "eggs" since both "bread" and "milk" have been removed

print(grocery_list)  # to print


"""Personal trials"""
game_points: list[int] = [102, 86, 94]

game_points[2]  # print out 94 OR [len(game_points) - 1]

game_points[1] = 72  # changes 86 to 72

len(game_points)  # print out then length of the list (3)

game_points.pop(1)  # removes 72, returns [102, 94]

print(game_points)  # to print


"""Anotha one"""
my_numbers: list[float] = list()  # or [] instead of list() for empty str

my_numbers.append(1.5)  # add 1.5 to the empty list (1 addition at a time)

print(my_numbers)  # to print


def display(list: list[int]) -> None:
    """To loop through a list and print out each individual value"""
    idx: int = 0
    while idx < len(list):
        print(list[idx])
        idx += 1
