#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the plusMinus function below.
def plusMinus(arr):
    p = float(0)
    ne = float(0)
    z = float(0)

    for i in range(n):
        if arr[i] > 0:
            p = p + 1
        elif arr[i] < 0:
            ne = ne + 1
        else:
            z = z + 1
    a = float((p / n))
    b = float((ne / n))
    c = float((z / n))

    print("%.6f" % a)
    print("%.6f" % b)
    print("%.6f" % c)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)




