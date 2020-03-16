#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'entryTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING keypad
#

def findIndexes(val, matrix):
    return [(index, row.index(val))
            for index, row in enumerate(matrix) if val in row][0]


def entryTime(s, keypad):
    # 1) translate keyboard string to a matrix
    kpMatrix = [[], [], []]
    count = 0
    index = 0
    for k in keypad:
        kpMatrix[index].append(k)
        count += 1
        if count > 2:
            index += 1
            count = 0
    # 2) initialize values and walk through input keys
    currKey = s[0]
    totalTime = 0
    for key in s:
        # 2.1) get current and next indexes in matrix
        currKeyIndex = findIndexes(currKey, kpMatrix)
        nextKeyIndex = findIndexes(key, kpMatrix)
        # 2.2) check if is same
        if currKeyIndex[0] == nextKeyIndex[0] and currKeyIndex[1] == nextKeyIndex[1]:
            currKey = key
            continue
        # 2.2) check if is same row
        elif currKeyIndex[0] == nextKeyIndex[0]:
            totalTime += abs(currKeyIndex[1] - nextKeyIndex[1])
        # 2.3) check if differs more than 1 row
        elif abs(currKeyIndex[0] - nextKeyIndex[0]) > 1:
            totalTime += 2
        # 2.4) check if differs exactly 1 row and differs less than 2 in column
        elif abs(currKeyIndex[0] - nextKeyIndex[0]) == 1 and abs(currKeyIndex[1] - nextKeyIndex[1]) < 2:
            totalTime += 1
        # 2.5) any other case falls here
        else:
            totalTime += 2
        currKey = key
    # 3) returns total time
    return totalTime


if __name__ == '__main__':
    s = '423692'
    keypad = '923857614'

    result = entryTime(s, keypad)
    print(result)
