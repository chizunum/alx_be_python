# polymorphism_demo.py
import math

# Base Class
class Shape:
    def area(self):
        """Method to be overridden by derived classes."""
        raise NotImplementedError("Subclasses must override this method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate area of rectangle: length × width."""
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate area of circle: π × radius²."""
        return math.pi * (self.radius ** 2)
