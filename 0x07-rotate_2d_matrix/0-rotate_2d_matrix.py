#!/usr/bin/python3
"""Contains the definition of the `rotate_2d_matrix` function"""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix in-place in a clockwise manner"""
    N = len(matrix)

    for x in range(int(N / 2)):
        for y in range(x, N - x - 1):
            temp = matrix[x][y]
            matrix[x][y] = matrix[N - y - 1][x]
            matrix[N - y - 1][x] = matrix[N - x - 1][N - y - 1]
            matrix[N - x - 1][N - y - 1] = matrix[y][N - x - 1]
            matrix[y][N - x - 1] = temp
