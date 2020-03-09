#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def countingValleys(n, s):
    level = 0
    nextLevel = 0
    result = 0
    for step in s:
        if step == 'U':
            nextLevel += 1
        else:
            nextLevel -= 1
        if level == 0 and nextLevel == -1:
            result += 1
        print(level, nextLevel)
        level = nextLevel
    return result


if __name__ == '__main__':
    result = countingValleys(8, ['U','D','D','D','U','D','U','U'])
    print(result)
