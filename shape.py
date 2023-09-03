"""Shape class, the parent of other classes"""

from abc import abstractmethod

class Shape():
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


# by Arman Azarnik
# armanazarnik@gmail.com
    