#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


#
# Complete the 'entryTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING keypad
#


def maximumClusterQuality(speed, reliability, maxMachines):
    best = 0
    n = len(speed)
    for i in range(1, maxMachines + 1):
        for x in range(n):
            speeds = []
            relias = []
            for q in range(x, x + i):
                print(q)
                speeds.append(speed[q])
                relias.append(reliability[q])
            print(speeds)
            print(relias)
            qual = reduce(lambda x, y: x+y, speeds) * min(relias)
            print(qual)
            if qual > best:
                best = qual
    return best


if __name__ == '__main__':
    speed = [12, 112, 100, 13, 55]
    reliability = [31, 4, 100, 55, 50]
    maxMachines = 3

    result = maximumClusterQuality(speed, reliability, maxMachines)
    print(result)
