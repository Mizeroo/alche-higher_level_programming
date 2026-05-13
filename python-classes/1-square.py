#!/usr/bin/python3
"""Module that defines a Square class."""
 
 
class Square:
    """Defines a square by its size."""
 
    def __init__(self, size):
        """Instantiate a Square with a size.
 
        Args:
            size (int): The size of the square.
        """
        self.__size = size
