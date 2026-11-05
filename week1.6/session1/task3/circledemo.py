# Week 1.6, Session 1: Task 3
import math
# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)
class Circle:
    def __init__(self, radius):
        if not isinstance(radius, int):
            return TypeError("wrong type")
        if not (radius > 0):
            return ValueError("not greater than 0")
        self.radius = radius

    def area(self):
        return math.pow(self.radius, 2) * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f", radius {self.radius}"