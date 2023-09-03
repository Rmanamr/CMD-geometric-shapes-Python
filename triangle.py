"""Triangle class, subclass of Shape class"""

from shape import Shape

class Triangle(Shape):
    count = 0
    def __init__(self, color = None, a = None, b = None ,c = None):
        super().__init__(color)
        self.set_sides(a, b, c)
        Triangle.count += 1

    def __del__(self):
        Triangle.count -= 1

    def get_shape(self):
        return "triangle"
    
    def get_color(self):
        return super().get_color()
        
    def get_sides(self):
        return self.side1, self.side2, self.side3
    
    def set_sides(self, a = None, b = None, c = None):
        if a is None or a<=0:
            self.side1 = 1
        else:
            self.side1 = a

        if b is None or b<=0:
            self.side2 = 1
        else:
            self.side2 = b

        if c is None or c<=0:
            self.side3 = 1
        else:
            self.side3 = c
        if self.side1+self.side2 == self.side3 or self.side1+self.side3 == self.side2 or self.side2+self.side3 == self.side1:
            return  None 
        

# by Arman Azarnik
# armanazarnik@gmail.com