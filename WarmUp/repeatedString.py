#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.


def repeatedString(s, n):
    inclusive = n // len(s)
    countA = s.count('a')
    totalA = inclusive * countA
    rest = n % len(s)
    if rest != 0:
        totalA += s[0 : rest].count('a')
    return totalA

if __name__ == '__main__':
    result = repeatedString('aba', 10)
    print(result)
