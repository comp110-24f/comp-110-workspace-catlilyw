"""Making a real wordle!"""

__author__ = "730655044"


def input_guess(secret_word_len: int) -> str:
    """Guess a word of a specific length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    if len(guess) == secret_word_len:
        return guess  # return not print because will be used in main function
    else:
        return input(f"That wasn't {secret_word_len} chars! Try again: ")


def contains_char(secret_word: str, char: str) -> bool:
    """Searching through the secret word for a specific character"""
    assert len(char) == 1
    index: int = 0
    while index < len(secret_word):
        if secret_word[index] == char:
            return True  # again need a return because will be utilized when iterating
            # -> through a word in main()
            exit()  # precautionary :)
        else:
            index = (
                index + 1
            )  # False return can't be in here otherwise it could return false
            # -> prematurely
    return False


def emojified(guess: str, secret: str) -> str:
    """Compare 2 strings to determine presence and position of characters"""
    WHITE_BOX: str = (
        "\U00002B1C"  # needed to capitalize since they're constants, had them as basic
        # -> local variables
    )
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    emoji: str = ""  # need this for the return of this function
    idx: int = 0
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            emoji += GREEN_BOX  # NOT a print statement like it would be with a normal
            # -> local variable as green_box
            idx += 1
        elif contains_char(secret, guess[idx]) and guess[idx] != secret[idx]:
            emoji += YELLOW_BOX
            idx += 1
        else:
            emoji += WHITE_BOX
            idx += 1
    return emoji  # the solution to all my problems


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    won: bool = (
        False  # need this to keep track of winning instead of putting guess as a local
        # -> variable outside the while loop
    )
    while turn <= 6 and not won:  # both must be true to continue in the loop
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(
            len(secret)
        )  # this local variable must be assigned WITHIN loop so it doesn't call
        # -> prematurely
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            won = True  # makes it so it doesn't print the "try again" statement
        turn += 1
    if not won:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
