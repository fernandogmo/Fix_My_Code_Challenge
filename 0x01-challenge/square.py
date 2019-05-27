#!/usr/bin/python3
""" Module (sloppily) defining a `Square` class """


class Square():
    """ `Square` class """

    """ default dimensions """
    width = 0
    height = 0

    def __init__(self, width, height):
        """ Ensure dimensions match """
        if width == height:
            self.width = width
            self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """ Perimeter of my square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation of Square instance """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
