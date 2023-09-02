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

        
"""Rectangle class, subclass of Shape"""
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


"""Square class, subclass of Shape and subclass of Rectangle"""
class Square(Rectangle):
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
       super().set_lenght(w)


#by Arman Azarnik
    