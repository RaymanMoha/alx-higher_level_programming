#!/usr/bin/python3
"""Defines a class Square."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square that inherits from class Rectangle"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """Initializes a new Square"""
        super().__init__(size, size, x, y, id)
        self.__size = size

    @property
    def size(self) -> int:
        """Size getter
        Returns the size(side) of the square
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """Size setter
        Sets the size of the square
        """
        self.__size = value
        self.width = self.height = value

    def __str__(self) -> str:
        """The __str__ method returns a string representation of the object
        return: The id, x, y, and size of the square."""
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[Square] ({}) {}/{} - {}".format(id, x, y, size)

    def update(self, *args, **kwargs):
        """Updates square arguments
        """
        attr = ['id', 'size', 'x', 'y']
        if args:
            for at, numb in zip(attr, args):
                setattr(self, at, numb)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)

    def to_dictionary(self) -> dict:
        """Square to dictionary
        Returns a dictionary representation of a Square instance
        return: A dictionary with id, size, x, and y of the square
        """
        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': size, 'y': y}
