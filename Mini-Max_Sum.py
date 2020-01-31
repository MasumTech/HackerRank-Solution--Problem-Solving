#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    rst = int(0)
    rst1 = int(0)

    for i in range(0, 4):
        rst1 = rst1 + arr[i]
    print(rst1, end=' ')

    for i in range(1, 5):
        rst = rst + arr[i]
    print(rst)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
