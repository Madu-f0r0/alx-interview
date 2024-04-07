#!/usr/bin/python3
"""Contains the definition of the function `validUTF8`"""


def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding"""
    for character in data:
        if character > 255:
            return False
    return True
