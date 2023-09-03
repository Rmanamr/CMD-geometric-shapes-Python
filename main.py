"""Object oriented shape class and subclasses, enter the shape's name, color and other attributes 
to construct them and calculate the area and perimeter"""

"""The main class for interacting with user"""

from shape import Shape
from circle import Circle
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from define import Define

def main():
    while(True):
        flag = True
        while(flag):
            shape = input("Enter shape name: ").lower()
            match shape:
                case "shape":
                    color = input("Enter color: ").lower()
                    if color == "":
                        color = None
                    newShape = Shape(color)
                    flag = False
                case "circle":
                    color = input("Enter color: ").lower()
                    if color == "":
                        color = None
                    radius = input("Enter radius: ")
                    if radius == "":
                        radius = None
                    else:
                        radius = float(radius)
                    newShape = Circle(color, radius)
                    flag = False
                case "triangle":
                    color = input("Enter color: ").lower()
                    if color == "":
                        color = None
                    side1 = input("Enter side1: ")
                    if side1 == "":
                        side1 = None
                    else:
                        side1 = float(side1)
                    side2 = input("Enter side2: ")
                    if side2 == "":
                        side2 = None
                    else: 
                        side2 = float(side2)
                    side3 = input("Enter side3: ")
                    if side3 == "":
                        side3 = None
                    else:
                        side3 = float(side3)
                    newShape = Triangle(color, side1, side2, side3)
                    flag = False
                case "rectangle":
                    color = input("Enter color: ").lower()
                    if color == "":
                        color = None
                    lenght = input("Enter  lenght: ")
                    if lenght == "":
                        lenght = None
                    else:
                        lenght = float(lenght)
                    width = input("Enter width: ")
                    if width == "":
                        width = None
                    else:
                        width = float(width)
                    newShape = Rectangle(color, lenght, width)
                    flag = False
                case "square":
                    color = input("Enter color: ").lower()
                    if color == "":
                        color = None
                    lenght = input("Enter lenght: ")
                    if lenght == "":
                        lenght = None
                    else:
                        lenght = float(lenght)
                    newShape = Square(color, lenght)
                    flag = False
                case _:
                    print("Shape not defined, try again")
        Define.define(newShape)


if __name__ == '__main__':
    main()


# by Arman Azarnik
# armanazarnik@gmail.com
    