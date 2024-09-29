def remove_chars(msg: str, char: str) -> str:
    """remove specific characters from a word"""
    idx: int = 0  # local variables
    copy: str = ""
    while idx < len(msg):
        if char != msg[idx]:
            copy = copy + msg[idx]
        idx += 1
    return copy


word: str = "yoyo"  # global variable
print(remove_chars(word, "y"))
print(remove_chars(word, "o"))
