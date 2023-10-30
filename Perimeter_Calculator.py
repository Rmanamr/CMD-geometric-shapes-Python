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
from Triangle import Triangle
from Rectangle import Rectangle
from Square import Square

class Perimeter_Calculator:
    """
    Get_perimeter class for calculating the perimeter of different geometric shapes.
    """
    def get_Perimeter(Shape):
        """
        function for calculating the perimeter of different geometric shapes.
        @param Shape: a geometric shape
        @type Shape: Shape object
        @return: calculated_Perimeter
        @rtype: double or string
        @examples: 
            circle_1 = new Circle(3)
            triangle_1 = new Triangle(2, 3, 4)
            rectangle_1 = new Rectangle(4, 6)
            square_1 = new Square(5)
        >>> get_Perimeter(circle_1)
            18.84955592153876
        >>> get_Perimeter(triangle_1)
            9.0
        >>> get_Perimeter(rectangle_1)
            20.0
        >>> get_Perimeter(square_1)
            20.0
        """
        calculated_Perimeter = 0.0
        if (isinstance(Shape, Circle)):
            calculated_Perimeter = Circle.get_radius(Shape) * 2 * math.pi
        
        elif (isinstance(Shape, Triangle)):
            a, b, c = Triangle.get_sides(Shape)
            calculated_Perimeter = a + b + c
        
        elif (isinstance(Shape, Rectangle)):
            calculated_Perimeter = (Rectangle.get_lenght(Shape) + Rectangle.get_width(Shape)) * 2
        
        elif (isinstance(Shape, Square)):
            calculated_Perimeter = Square.get_lenght(Shape) * 4
        
        else:
            calculated_Perimeter = "Shape not defiend"

        return calculated_Perimeter 