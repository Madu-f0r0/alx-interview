#!/usr/bin/python3
"""Contains the description of the `island_perimeter` function
"""


def island_perimeter(grid):
    """Defines the perimeter of a single island in a grid
    """
    perimeter = 0
    islandAlreadyFound = False

    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[x]) - 1):
            topSideIsWater = rightSideIsWater = False
            bottomSideIsWater = leftSideIsWater = False

            if grid[x][y] == 1:
                if islandAlreadyFound is True:
                    return 0
                if grid[x - 1][y] == 0:
                    perimeter += 1
                    topSideIsWater = True
                if grid[x][y + 1] == 0:
                    perimeter += 1
                    rightSideIsWater = True
                if grid[x + 1][y] == 0:
                    perimeter += 1
                    bottomSideIsWater = True
                if grid[x][y - 1] == 0:
                    perimeter += 1
                    leftSideIsWater = True

                if topSideIsWater and rightSideIsWater:
                    if bottomSideIsWater and leftSideIsWater:
                        islandAlreadyFound = True

    return perimeter
