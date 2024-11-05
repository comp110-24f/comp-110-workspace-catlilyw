"""Checking my point function!"""

# importing the type to test it

from CQs.cq09.point import Point

# from CQs.cq09.point import scale_by

my_point: Point = Point(1.0, 2.0)

print(my_point.scale_by(2))  # outputs (2.0, 4.0)! functions properly!
print(f"({my_point.x}, {my_point.y})")  # outputs (1.0, 2.0)! does not get mutated
