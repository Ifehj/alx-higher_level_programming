#!/usr/bin/ython3
""" Returns all attribute and omethods of the object
@obj: object to check
 """


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return (dir(obj))
