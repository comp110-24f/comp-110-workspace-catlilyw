"""Dictionary work for ex06"""

__author__ = "730655044"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Flip the keys and the values"""
    inverted: dict[str, str] = {}
    duplicates: list[str] = []
    for key in original:  # checking if the NEW keys are duplicates
        if (
            original[key] in duplicates
        ):  # new keys will be the values, so use subscrip notation to access those
            raise KeyError("uh oh key error!")
        else:
            duplicates.append(original[key])
    for key in original:
        inverted[original[key]] = (
            key  # key of inverted is the value of original, and value is equal to the
            # key of original
        )
    return inverted


def favorite_color(names_colors: dict[str, str]) -> str:
    """Return the most common favorite color"""
    color_counter: dict[str, int] = {}
    popular_color: str = ""  # trying to start with an empty str
    if popular_color == "":
        color_counter[popular_color] = 0  # making it so an empty str can be usable
    for key in names_colors:
        if names_colors[key] in color_counter:
            color_counter[
                names_colors[key]
            ] += 1  # new dictionary keeping track of count of each color
        else:
            color_counter[names_colors[key]] = 1  # initializing the portions of the
    for color in color_counter:  # once it has data
        if color_counter[color] > color_counter[popular_color]:
            popular_color = color  # needs to = the key not the value
    return popular_color


def count(input: list[str]) -> dict[str, int]:
    """Count all the instances of a specific key in the dictionary"""
    new_dict: dict[str, int] = {}  # start an empty dict
    for key in input:
        if key in new_dict:
            new_dict[key] += 1  # increase the value
        else:
            new_dict[key] = 1  # establish the initial value
    return new_dict


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Creates lists of all of the words that start with specific letters"""
    output_dict: dict[str, list[str]] = {}
    for string in input:
        string.lower()  # makes each str lowercase in its entirety
        if string[0] in output_dict:
            output_dict[string[0]] += [
                string
            ]  # put the elem (str) in a list at the desired key (str[0]), must make
            # str a list [str]
        else:
            output_dict[string[0]] = [string]
    return output_dict


def update_attendance(inputdict: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance dict"""
    if day in inputdict:
        if student not in inputdict[day]:
            inputdict[day].append(student)
    else:
        inputdict[day] = [student]  # adding the student and the day
