"""Challenge question 9 with OOPs"""

__author__ = "730655044"


class Point:
    """My new class/type!"""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Using the constructor to define what happens when new object is created"""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int):
        """Returning an updated version of Point after multiplied by a factor"""
        # new_point : Point = Point(self.x, self.y)
        # self.x *= factor  # making the x float of the return value
        # self.y *= factor  # making the y float of the return value
        return f"({self.x * factor}, {self.y * factor})"  # only need a return statement
        # return new_point
