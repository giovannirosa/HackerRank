#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def rotLeft(a, d):
    b = a.copy()
    n = len(a)
    for i in range(n):
        pos = i - d
        if pos < 0:
            pos = n + pos
        b[pos] = a[i]
    return b


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    #arr = [5, 1, 2, 3, 4]

    result = rotLeft(arr, 4)

    print(result)
