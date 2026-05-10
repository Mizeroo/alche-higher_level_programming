#!/usr/bin/python3
"""Defines a Square class with size validation."""


class Square:
    """Represents a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initializes a new Square with an optional size.

        Args:
            size (int): the size of the square, defaults to 0.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Computes and returns the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size * self.__size