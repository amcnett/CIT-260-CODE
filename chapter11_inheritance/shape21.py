# Inheritance Exercise
import math
from typing import override
# To do:
# (1) Make Circle drive from Shape
# (2) Note that a Circle object will have a radius. Initialize this attribute.
# (3) In Circle, override the area function in shape so that it returns the area of the circle (pi * radius ** 2).
# Test this by creating a circle object
# (4) Create a rectangle class that derives from Shape. It should have length and width properties.

class Shape:
    def __init__(self, color):
        self._color = color  # note this has "protected" status

    def area(self):
        raise NotImplementedError("Subclasses must implement the area method.")

    def info(self):
        return f"This is a shape of color {self.color}."

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.__radius = radius

    @override
    def area(self):
        return math.pi * self.__radius ** 2


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.__length = length
        self.__width = width

    @override
    def area(self):
        return self.__length * self.__width 

acircle = Circle("green", 4)
print(acircle.area())

arect = Rectangle("yellow", 10, 100)
print(arect.area())