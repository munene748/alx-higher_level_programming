#!/usr/bin/python3
"""Replicate what the example is doing. haaard"""

import math


class MagicClass:
    """Represents a magic class."""

    def __init__(self, radius=0):
        """Initialize a new MagicClass instance.

        Args:
            radius (int or float): The radius of the circle.0 as def.
        """
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """Get/set the radius of the circle."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle.

        Args:
            value Float/int: The radius value to set.

        Raises:
            TypeError: If value is not a number. float or int.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = value

    def area(self):
        """Calculate and return the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.__radius


if __name__ == "__main__":
    # Test the MagicClass implementation
    magic_circle = MagicClass(5)
    print("Area:", magic_circle.area())
    print("Circumference:", magic_circle.circumference())
