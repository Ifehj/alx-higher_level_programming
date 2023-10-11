#!/usr/bin/python3
""" is_same_class checks if the objest is an instance of the 
specified class """


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return (type(obj) is a_class)
