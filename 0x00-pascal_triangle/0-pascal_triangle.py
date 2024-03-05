#!/usr/bin/python3
def pascal_triangle(n):
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
