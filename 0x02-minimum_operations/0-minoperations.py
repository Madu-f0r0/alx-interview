#!/usr/bin/python3
"""This module contains the `minOperations()` function"""


def minOperations(n: int) -> int:
    """Calculates the minimum number of operations requuired to result
    in a specified number of `H` characters in a file using only the
    `Copy All` and `Paste` operations
    """
    fileContent = 'H'
    copiedText = ''
    noOfOperations = 0

    while len(fileContent) < n:
        if n % len(fileContent) == 0:
            copiedText = fileContent
            noOfOperations += 1
        fileContent = fileContent + copiedText
        noOfOperations += 1
    return noOfOperations
