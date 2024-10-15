"""Summing the elements of a list using different loops"""

__author__ = "730655044"


def w_sum(vals: list[float]) -> float:
    """Use a while loop to sum all the values in a list of floats"""
    idx: int = 0
    sum_vals: float = 0
    while idx < len(vals):
        sum_vals += vals[idx]
        idx += 1
    return sum_vals


def f_sum(vals: list[float]) -> float:
    """Use a for...in... list to sum all the values in a list of floats"""
    sum_vals: float = 0
    for elem in vals:  # no control over range, just goes through every item
        sum_vals += elem
    return sum_vals


def f_range_sum(vals: list[float]) -> float:
    """Use a for...in(range)... loop to sum all the values of a list of floats"""
    sum_vals: float = 0
    for idx in range(0, len(vals)):  # relate it to idx so elems get added even if
        # they are higher than the value of the length of the vals list
        sum_vals += vals[idx]
        idx += 1
    return sum_vals
