#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def hourglassSum(arr):
    maxSum = 0
    init = True
    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            hSum = arr[i][j]
            hSum += arr[i][j + 1]
            hSum += arr[i][j + 2]
            hSum += arr[i + 1][j + 1]
            hSum += arr[i + 2][j]
            hSum += arr[i + 2][j + 1]
            hSum += arr[i + 2][j + 2]
            if hSum > maxSum or init:
                maxSum = hSum
                init = False
    return maxSum


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    result = hourglassSum(arr)
