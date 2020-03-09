#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def jumpingOnClouds(c):
    index = 0
    steps = 0
    while index < len(c) - 1:
        if index + 2 <= len(c) - 1 and c[index + 2] == 0:
            index += 2
        else:
            index += 1
        steps += 1
    return steps

if __name__ == '__main__':
    result = jumpingOnClouds([0, 0, 1, 0, 0, 1, 0])
    print(result)
