#!/usr/bin/python3
""" Implementation of Pascals Triangle Algorithm """


def pascal_triangle(n):
    """ Implements Pascal's Triangle
    Parameter:
    n: (int) the number of rows in the triangle
    Returns: An empty list if n <= 0, or a list of list
    Each inner list contains the values in a row
    """
    triangle = []

    for r in range(n):
        rowList = []

        for c in range(r + 1):
            if c == 0 or c == r:
                rowList.append(1)
            else:
                rowList.append(triangle[r - 1][c - 1] + triangle[r - 1][c])

        triangle.append(rowList)

    return triangle
