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


def maxHeight(wallPositions, wallHeights):
    print(wallPositions, wallHeights)
    wallTotalHeights = []
    wallTotalPositions = []
    lastWallPos = 0
    lastWallIndex = 0
    for index, wall in enumerate(wallPositions):
        if lastWallPos != 0:
            for mud in range(lastWallPos, wall - 1):
                wallTotalHeights.append(0)
                wallTotalPositions.append('mud')
        lastWallPos = wall
        lastWallIndex = index
        wallTotalHeights.append(wallHeights[index])
        wallTotalPositions.append('wall')
    wallTotalPositionsSave = wallTotalPositions.copy()
    print(wallTotalHeights, wallTotalPositions)

    while 'mud' in wallTotalPositions:
        for index, height in enumerate(wallTotalHeights):
            print(index, height)
            if wallTotalPositions[index] == 'wall':
                if index > 0 and wallTotalPositions[index - 1] == 'mud':
                    mudIndex = index - 1
                    leftHeight = wallTotalHeights[mudIndex - 1]
                    rightHeight = height
                    if leftHeight == 0 or leftHeight == rightHeight or leftHeight - rightHeight > 0:
                        wallTotalHeights[mudIndex] = rightHeight + 1
                    elif leftHeight - rightHeight < 0:
                        wallTotalHeights[mudIndex] = rightHeight
                if index < len(wallTotalHeights) - 1 and wallTotalPositions[index + 1] == 'mud':
                    mudIndex = index + 1
                    leftHeight = height
                    rightHeight = wallTotalHeights[mudIndex + 1]
                    if rightHeight == 0 or leftHeight == rightHeight or rightHeight - leftHeight > 0:
                        wallTotalHeights[mudIndex] = leftHeight + 1
                    elif rightHeight - leftHeight < 0:
                        wallTotalHeights[mudIndex] = leftHeight
        for index, height in enumerate(wallTotalHeights):
            if height != 0:
                wallTotalPositions[index] = 'wall'
        print(wallTotalHeights, wallTotalPositions)
    for index, height in enumerate(wallTotalHeights):
        if index > 0 and height - wallTotalHeights[index - 1] > 1:
            wallTotalHeights[index - 1] = wallTotalHeights[index - 1] + 1
        if index < len(wallTotalHeights) - 1 and height - wallTotalHeights[index + 1] < -1:
            wallTotalHeights[index + 1] = height + 1
    print(wallTotalHeights)
    maxMudHeight = 0
    for index, height in enumerate(wallTotalHeights):
        if wallTotalPositionsSave[index] == 'mud' and height > maxMudHeight:
            maxMudHeight = height
    return maxMudHeight


if __name__ == '__main__':
    wallPositions = [1, 10]
    wallHeights = [1, 5]

    result = maxHeight(wallPositions, wallHeights)
    print(result)
