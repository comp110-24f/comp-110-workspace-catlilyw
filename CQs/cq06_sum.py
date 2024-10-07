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
    for elem in vals:
        sum_vals += elem
    return sum_vals


def f_range_sum(vals: list[float]) -> float:
    """Use a for...in(range)... loop to sum all the values of a list of floats"""
    sum_vals: float = 0
    idx: int = 0
    for idx in range(0, len(vals) - 1):
        sum_vals += vals[idx]
        idx += 1
    return sum_vals


print(f_range_sum([1.0, 2.3, 4.6, 3.1]))
