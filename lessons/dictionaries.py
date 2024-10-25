"""Practice with dictionaries"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

# len evaluates to number of key-value entries
print(len(ice_cream))

# add key-value entries using subscription notation
ice_cream["mint"] = 10

# access values by their key using sub notation
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# reassign values by their key using assignment operators
ice_cream["mint"] += 1

# remove items by using the pop method
ice_cream.pop("strawberry")

# test if a key is in the dictionary
print("strawberry" in ice_cream)
print("vanilla" in ice_cream)

# loop through items using for-in loops
for flavor in ice_cream:
    count: int = ice_cream[flavor]
    print(f"{flavor}: {count}")


my_dictionary: dict[str, float] = {}

msg: dict[str, int] = {"Hello": 1, "Y'all": 2}
msg["Y'all"] += 3

ids: dict[int, str] = {100: "Alyssa", 200: "Carmine"}
len(ids)
ids.pop(100)

inventory: dict[str, int] = {"pens": 10, "notebooks": 5, "erasers": 8}
inventory["markers"] = 15

prices: dict[str, float] = {"bread": 2.99, "milk": 1.99, "eggs": 3.49}
prices["milk"] = 2.50

scores: dict[str, int] = {"Alice": 85, "Bob": 90, "Charlie": 88}
for elem in scores:
    print(elem)


def sum(score: dict[str, int]) -> int:
    total_score: int = 0
    for elem in score:
        total_score += score[elem]
