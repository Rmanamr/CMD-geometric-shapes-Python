"""Python CMD program, object-oriented shape class and subclasses, enter the shape's name, color and other attributes 
to construct them and calculate the area and perimeter.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

from Rectangle import Rectangle

class Square(Rectangle):
    """
    Square class, subclass of Shape class and subclass of Rectangle class.
    """
    count = 0
    def __init__(self, color, l = None):
        super().__init__(color, l, l)
        Square.count += 1

    def __del__(self):
        Square.count -= 1

    def get_shape(self):
        return "square"
    
    def get_color(self):
        return super().get_color()
      
    def get_lenght(self):
        return self.lenght
    
    def get_width(self):
        return self.width
    
    def set_lenght(self, l = None):
        super().set_lenght(l)

    def set_width(self, w = None):
       super().set_width(w)