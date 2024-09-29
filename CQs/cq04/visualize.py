"""Importing the functions to see what's going on!"""

__author__ = "730655044"


from concatenation import concat
from coordinates import (
    get_coords,
)  # had to add to a path for the module to be accessible


x: str = "123"
y: str = "abc"

concat(x, y)
get_coords(x, y)
