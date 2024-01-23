#!/usr/bin/python3
"""Square class that has size"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        if isinstance(size, int) and size >= 0:
            self.__size = size
        elif int(size) < 0:
            raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """# returns square area"""
        return self.__size ** 2
