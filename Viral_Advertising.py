#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the viralAdvertising function below.
def viralAdvertising(n):
    ad = int(5)
    rst = int(0)
    for i in range(n):
       like = int(ad/2)
       ad = (like*3)
       rst = rst + like
    return rst


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
