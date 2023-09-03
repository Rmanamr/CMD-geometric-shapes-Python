"""Get_area class to claculate the area of different shapes"""

import math
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from get_perimeter import Get_Perimeter

class Get_Area:
    def get_area(Shape):
        if (isinstance(Shape, Circle)):
            return Circle.get_radius(Shape)**2*math.pi
        elif (isinstance(Shape, Triangle)):
            a, b, c = Triangle.get_sides(Shape)
            "Heron's formula for triangle area"
            semi_perimeter = Get_Perimeter.get_perimeter(Shape)/2
            return (math.sqrt(abs(semi_perimeter*(semi_perimeter - a)*(semi_perimeter - b)* (semi_perimeter - c))))
        elif (isinstance(Shape, Rectangle)):
            return Rectangle.get_width(Shape)*Rectangle.get_lenght(Shape)
        elif (isinstance(Shape, Square)):
            return Square.get_lenght(Shape)**2
        else:
            return "Shape not defiend"


# by Arman Azarnik
# armanazarnik@gmail.com
    