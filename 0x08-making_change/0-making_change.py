#!/usr/bin/python3
"""This module contains the definition of the `makeChange` method
"""


def makeChange(coins, total):
    """Returns the fewest number of specified coins required to
    make change for a given amount
    """
    coins.sort(reverse=True)
    noOfCoins = 0

    if total <= 0:
        return 0
    for coin in coins:
        while total >= coin:
            noOfCoins += int(total / coin)
            total %= coin

    if total > 0:
        return -1
    return noOfCoins
