"""Chardle or wordle or what have you"""

__author__ = "730655044"


def main() -> None:
    """Calling contains_char"""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """The word that the player will input."""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        print("'" + word + "'")  # add ' to match format
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        print("'" + word + "'")  # 2 print statements to get desired output
    return word


def input_letter() -> str:
    """Prompts the user to enter a single character."""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        print("'" + letter + "'")
    else:
        print("Error: Character must be a single character.")
        exit()
        print("'" + letter + "'")  # exits before this prints, was useful in first step
    return letter


def contains_char(word: str, letter: str) -> None:
    """To look for the letter in the word."""
    print("Searching for " + letter + " in " + word)
    index: int = 0
    count: int = 0
    while index < len(
        word
    ):  # < word rather than <= to word because all indeces=len(word)-1
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count += 1  # add to count when letter is found
            index = index + 1
        else:
            index += 1
    if (
        count == 0
    ):  # start a new block not a while loop so you don't get in an infinite loop
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
