# 4. create a base class called Shape and then create child classes like Circle and Rectangle.
# Implement methods for calculating area and perimeter, and show how inheritance can be used
# effectively.

pi = 2.14

class Shape:
    def ___init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, diameter):
        self.diameter = diameter
    
    def calculate_perimeter(self, diameter):
        perimeter = pi * diameter
        return perimeter
    
    def calculate_area(diameter):
        area = pi * (diameter/2) ** 2
        return area

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def calculate_perimeter(self, length, breadth):
        perimeter = 2(length + breadth)
        return perimeter

    def calculate_area(length,breadth):
        area = length * breadth
        return area