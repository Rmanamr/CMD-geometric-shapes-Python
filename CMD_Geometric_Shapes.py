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
from Square import Square
from Introducer import Introducer
from Triangle import Triangle
from Rectangle import Rectangle

def main():
    """
    The main class for interacting with user.
    """
    while(True):
    # while loop to keep the program running
        
        flag = True
        while(flag):
         # while loop to keep the program running
            
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
                    print("Shape not defined, try again.")

        print(Introducer.introduce(newShape))


if __name__ == '__main__':
    main()
    # run the main function after executing this file