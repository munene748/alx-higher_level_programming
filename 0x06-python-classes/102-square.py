#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int or float): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int or float): The size value to set.

        Raises:
            TypeError: If value is not a number (int or float).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the behavior for the equality comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the behavior for the inequality comparison."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the behavior for the less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the behavior for the less than or equal comparison."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the behavior for the greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the behavior for the greater than or equal comparison."""
        return self.area() >= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
