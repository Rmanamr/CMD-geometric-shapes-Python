"""Define class to define different shape's attrebutes"""

from shape import Shape
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from get_perimeter import Get_Perimeter
from get_area import Get_Area

class Define:
    def define(shape):
        if (isinstance(shape, (Circle, Triangle, Rectangle, Square))):
            print("I am a %s %s whith area of %.4f and primeter of %.4f." % (shape.get_color(), shape.get_shape(), Get_Area.get_area(shape), Get_Perimeter.get_perimeter(shape)))
        elif(isinstance(shape,Shape)):
            print("I am a %s %s." % (shape.get_color(), shape.get_shape()))
        else:
            print("Shape not defiend")


#by Arman Azarnik
    