#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """
    A class Rectangle that defines a rectangle by:
    Private instance attribute: width and height.
    Optional instantiation with width=0 and height=0.
    Public instance methods: area and perimeter.
    Public class attribute: number_of_instances, incremented/decremented during each instantiation/deletion.
    Public class attribute: print_symbol, used as symbol for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance with optional width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rect = []
            for i in range(self.height):
                rect.append(str(self.print_symbol) * self.width)
            return "\n".join(rect)

    def __repr__(self):
        """Return a string representation of the rectangle for recreation."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
