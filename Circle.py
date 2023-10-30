"""Python CMD program, object-oriented shape class and subclasses, enter the shape's name, color and other attributes 
to construct them and calculate the area and perimeter.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""
        
from Shape import Shape

class Circle(Shape):
    """
    Circle class, subclass of Shape class
    """
    count = 0
    def __init__(self, color = None, r = None):
        super().__init__(color)
        self.set_radius(r)
        Circle.count += 1
        
    def __del__(self):
        Circle.count -= 1

    def get_shape(self):
        return "circle"

    def get_color(self):
        return super().get_color()

    def get_radius(self):
        return self.radius
    
    def set_radius(self, r = None):
        if r is None or r<0:
            self.radius = 1
        else:
            self.radius = r