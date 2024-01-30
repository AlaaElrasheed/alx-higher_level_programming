#!/usr/bin/python3
"""Module for printing a square with a given size"""


def print_square(size):
    """
    Prints a square
    Arga:
        size (int): defines the size of square
    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
        ValueError: size must be an integer
    Returns:
        None
    """
    if not isinstance(size, int) or (not isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        if i != size:
            print()


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
