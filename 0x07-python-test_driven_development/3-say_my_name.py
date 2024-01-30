#!/usr/bin/python3
""" Module for printing Full names"""


def say_my_name(first_name, last_name=""):
    """function that prints full name

    Args:
        first_name: first name to be printed
        last_name: last name to be printed

    Raises:
        TypeError: if one of the names is not string

    Returns:
        no return void function.

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
