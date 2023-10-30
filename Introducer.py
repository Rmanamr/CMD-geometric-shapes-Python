"""Python CMD program, object-oriented shape class and subclasses, enter the shape's name, color and other attributes 
to construct them and calculate the area and perimeter.
using Python version 3.11.4
@version : 1.0
@license: MIT License
@author : Arman Azarnik
contact me at : armanazarnik@gmail.com
"""

from Shape import Shape
from Circle import Circle
from Triangle import Triangle
from Rectangle import Rectangle
from Square import Square
from Perimeter_Calculator import Perimeter_Calculator
from Area_Calculator import Area_Calculator

class Introducer:
    """    
    Introducer class to introduce different shape's attrebutes.
    """
    def introduce(shape):
        """
        function for introducing the shape's color, name, area and perimeter.
        @param Shape: a geometric shape
        @type Shape: Shape object
        @return: introduce_String
        @rtype: string
        @examples: 
            circle_1 = new Circle(red, 3)
            triangle_1 = new Triangle(blue, 2, 3, 4)
            rectangle_1 = new Rectangle(green, 4, 6)
            square_1 = new Square(5)
        >>> introduce(circle_1)
            I am a red circle whith area of 28.2743 and primeter of 18.8496.
        >>> introduce(triangle_1)
            I am a blue triangle whith area of 2.9047 and primeter of 9.0000.
        >>> introduce(rectangle_1)
            I am a green rectangle whith area of 24.0000 and primeter of 20.0000.
        >>> introduce(square_1)
            I am a pink square whith area of 25.0000 and primeter of 20.0000.
        """
        if (isinstance(shape, (Circle, Triangle, Rectangle, Square))):
            introduce_String = "I am a %s %s whith area of %.4f and primeter of %.4f." % (shape.get_color(), shape.get_shape(), 
                Area_Calculator.get_Area(shape), Perimeter_Calculator.get_Perimeter(shape))
            
        elif(isinstance(shape,Shape)):
            introduce_String = "I am a %s %s." % (shape.get_color(), shape.get_shape())

        else:
            introduce_String = "Shape not defiend"

        return introduce_String