"""Get_perimeter class for calculating the perimeter of different shapes"""

import math
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle
from square import Square

class Get_Perimeter:
    def get_perimeter(Shape):
        if (isinstance(Shape, Circle)):
            return Circle.get_radius(Shape)*2*math.pi
        elif (isinstance(Shape, Triangle)):
            a, b, c = Triangle.get_sides(Shape)
            return a+b+c
        elif (isinstance(Shape, Rectangle)):
            return (Rectangle.get_lenght(Shape)+Rectangle.get_width(Shape))*2
        elif (isinstance(Shape, Square)):
            return Square.get_lenght(Shape)*4
        else:
            return "Shape not defiend"


#by Arman Azarnik
    