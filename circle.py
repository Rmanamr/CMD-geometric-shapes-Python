"""Circle class, subclass of Shape class"""

from shape import Shape

class Circle(Shape):
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


# by Arman Azarnik
# armanazarnik@gmail.com

