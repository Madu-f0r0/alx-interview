#!/usr/bin/env python3
"""This script parses a log and outputs its metrics"""

import sys

# Status codes being checked
statusCodesFrequency = {'200': 0, '301': 0, '400': 0, '401': 0,
                        '403': 0, '404': 0, '405': 0, '500': 0}

totalFileSize = 0
lineCounter = 0

# Read stdin input line by line
for line in sys.stdin:
    lineCounter += 1
    parsedInputLine = line.split(' ')

    # Confirm input format
    if len(parsedInputLine) == 9:
        fileSize = int(parsedInputLine[-1])
        statusCode = parsedInputLine[-2]

        totalFileSize += fileSize

        # Confirm that status code in the input is being checked
        if statusCode in statusCodesFrequency.keys():
            statusCodesFrequency[statusCode] += 1

        # Print total file size after every 10 input lines
        if lineCounter == 10:
            lineCounter = 0
            print("File size: {}".format(totalFileSize))
            for code, frequency in statusCodesFrequency.items():
                if frequency > 0:
                    print("{}: {}".format(code, frequency))