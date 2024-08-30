"""Tea party exercise!"""

__author__: str = "730655044"


def main_planner(guests: int) -> None:
    """outlines the amount of guests at the party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))

    # for "print("Cost")...", define the initial parameters of cost (tea_count and
    # -> treat_count) by making the functions that account for those values have the one
    # -> generic defined input (guests).


def tea_bags(people: int) -> int:
    """the number of tea bags needed for the party"""
    return people * 2


def treats(people: int) -> int:
    """the number of treats needed for the party"""
    return int(1.5 * (tea_bags(people=people)))


# keyword argument used-- format= func(parameter=x)

# because each person needs 2 tea_bags, one person = 2 tea_bags, and therefore 3 treats
# -> therefore, multiply tea_bags function by 1.5
# -> this will result in a proportion of 3 treats per 2 tea_bags


def cost(tea_count: int, treat_count: int) -> float:
    """the cost of all of the tea_bags and treats needed"""
    return (tea_count * 0.50) + (treat_count * 0.75)


"""Making the program runable!"""

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
