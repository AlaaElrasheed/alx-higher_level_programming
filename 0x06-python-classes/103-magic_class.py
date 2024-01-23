#!/usr/bin/python3
"""defines advanced task in magic calculation"""


import math


class MagicClass:
    """represents a circle"""

    def __init__(self, radius=0):
        """ ekffpwkfasfw
        Args:
        radius (float or int): blah blah
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ return area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """return circumference"""
        return (2 * math.pi * self.__radius)
