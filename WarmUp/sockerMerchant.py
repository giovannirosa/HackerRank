#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    result = 0
    while len(ar) > 0:
        i = ar.pop()
        try:
            j = ar.index(i)
        except:
            print('not found')
            continue
        del ar[j]
        print(i)
        result += 1
    return result


if __name__ == '__main__':
    result = sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
    print(result)
