#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the square with a size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
