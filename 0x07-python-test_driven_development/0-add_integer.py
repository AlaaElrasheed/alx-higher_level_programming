#!/usr/bin/python3
"""This is the first task to test driven development"""


def add_integer(a, b=98):
    """function for adding numbers

    Args:
        a (int): first element
        b (int): second element

    Raises:
        TypeError: if a, b are not int or float

    Returns:
        the sum of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")