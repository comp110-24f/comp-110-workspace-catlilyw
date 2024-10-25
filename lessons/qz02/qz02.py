def diclength(input: list[str]) -> dict[str, int]:
    """Return a dictionary with strings as keys, and the lengths of the str as vals"""
    lengthd: dict[str, int] = {}
    for elem in input:
        lengthd[elem] = len(elem)
    # for idx in range(0, len(input))
    # lengthd[input[idx]] = len(input[idx])
    return lengthd
