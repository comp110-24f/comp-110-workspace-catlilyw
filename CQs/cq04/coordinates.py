"""Finding the formatted pairs of each character"""

__author__ = "730655044"


def get_coords(xs: str, ys: str) -> None:
    xindex: int = 0
    while xindex < len(xs):

        yindex: int = 0
        while yindex < len(ys):
            print(f"({xs[xindex]}, {ys[yindex]})")
            yindex += 1  # += not =+ dummy

        xindex += 1
