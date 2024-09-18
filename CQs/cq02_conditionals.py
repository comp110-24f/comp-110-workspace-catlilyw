"""Practice with conditionals, local variables, and user input!"""

__author__ = "730655044"


def guess_a_number() -> None:
    """Guess a number to see if it matches the secret number"""
    secret: int = 7
    guess: str = input(
        "Guess a number: "
    )  # create local variable for guess by following same format
    print(
        "Your guess was " + guess
    )  # keep print statement in the function body so "guess" can be found
    if (
        int(guess) == secret
    ):  # turn guess into an integer so it can be compared to the integer "secret"
        print("You got it!")
    elif int(guess) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "main":
    guess_a_number()
