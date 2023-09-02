"""Rectangle class, subclass of Shape"""

from shape import Shape
from abc import abstractmethod

class Rectangle(Shape):
    count = 0
    def __init__(self, color, l = None , w = None):
        super().__init__(color)
        self.set_lenght(l)
        self.set_width(w)
        Rectangle.count += 1

    def __del__(self):
        Rectangle.count -= 1
            
    def get_shape(self):
        return "rectangle"
    
    def get_color(self):
        return super().get_color()

    @abstractmethod
    def get_lenght(self):
        return self.lenght
    
    @abstractmethod
    def get_width(self):
        return self.lenght
    
    def set_lenght(self, l = None):
        if l == None or l <= 0:
            self.lenght = 1
        else:
            self.lenght = l

    def set_width(self, w = None):
        if w == None or w <= 0:
            self.width = 1
        else:
            self.width = w


#by Arman Azarnik
    