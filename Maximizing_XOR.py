#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    mx = 0
    for i in range(l,r+1):
        for j in range(i, r+1):
        #   print(i,j,i^j)
          if mx< i^j:
            mx = i^j
    return mx
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()