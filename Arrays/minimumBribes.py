#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.


def minimumBribes(q):
    n = 0
    for i, x in enumerate(q):
        if i == len(q) - 1:
            break
        if x - (i + 1) > 2:
            print('Too chaotic')
            return
        p = q[i + 1:]
        if min(p) < x:
            n += len([k for k in p if k < x])
    print(n)


if __name__ == '__main__':
    q = [1, 2, 5, 3, 7, 8, 6, 4]

    minimumBribes(q)
