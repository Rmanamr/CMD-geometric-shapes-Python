"""Python CMD program, object-oriented shape class and subclasses, enter the shape's name, color and other attributes 
to construct them and calculate the area and perimeter.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

from abc import abstractmethod

class Shape():
    """
    Shape class, the parent of other geometric shape classes.
    """
    count = 0
    def __init__(self, color = None):
        self.set_color(color)
        Shape.count += 1
    
    @abstractmethod
    def __del__(self):
        Shape.count -=1

    @abstractmethod
    def get_shape(self):
        return "shape"

    @abstractmethod 
    def get_color(self):
        return self.color
    
    @abstractmethod
    def set_color(self, color = None):
        if color is None:
            color = "nocolor"
        self.color = color 