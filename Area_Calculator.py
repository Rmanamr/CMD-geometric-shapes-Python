"""Python CMD program, object-oriented shape class and subclasses, enter the shape's name, color and other attributes 
to construct them and calculate the area and perimeter.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

import math
from Circle import Circle
from Square import Square
from Triangle import Triangle
from Rectangle import Rectangle
from Perimeter_Calculator import Perimeter_Calculator

class Area_Calculator:
    """
    Area_Calculator class to claculate the area of different geometric shapes.
    """
    def get_Area(Shape):
        """
        function for calculating the area of different geometric shapes.
        @param Shape: a geometric shape
        @type Shape: Shape object
        @return: calculated_Area
        @rtype: double or string
        @examples: 
            circle_1 = new Circle(3)
            triangle_1 = new Triangle(2, 3, 4)
            rectangle_1 = new Rectangle(4, 6)
            square_1 = new Square(5)
        >>> get_Area(circle_1)
            28.274333882308138
        >>> get_Area(triangle_1)
            2.9047375096555625
        >>> get_Area(rectangle_1)
            24.0
        >>> get_Area(square_1)
            25.0
        """
        calculated_Area = 0.0
        if (isinstance(Shape, Circle)):
            calculated_Area = Circle.get_radius(Shape) ** 2 * math.pi
        
        elif (isinstance(Shape, Triangle)):
            a, b, c = Triangle.get_sides(Shape)
            semi_perimeter = Perimeter_Calculator.get_Perimeter(Shape) / 2
            # Heron's formula for triangle area
            calculated_Area = (math.sqrt(abs(semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c))))
        
        elif (isinstance(Shape, Rectangle)):
            calculated_Area = Rectangle.get_width(Shape) * Rectangle.get_lenght(Shape)
        
        elif (isinstance(Shape, Square)):
            calculated_Area = Square.get_lenght(Shape) ** 2

        else:
            calculated_Area = "Shape not defiend"
        
        return calculated_Area