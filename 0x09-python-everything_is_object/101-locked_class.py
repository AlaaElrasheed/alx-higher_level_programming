#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    prevents any other classes to get an attr besides first class
    """

    __slots__ = ["first_name"]
