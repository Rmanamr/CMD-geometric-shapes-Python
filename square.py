"""Square class, subclass of Shape and Rectangle"""

from rectangle import Rectangle

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
    