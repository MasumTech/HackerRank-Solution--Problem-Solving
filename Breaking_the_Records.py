#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    mn = int(scores[0])
    cmn = int(0)
    mx = int(scores[0])
    cmx = int(0)
    for i in range(1, len(scores)):
        if scores[i] < mn:
            cmn += 1
            mn = scores[i]
        if scores[i] > mx:
            cmx += 1
            mx = scores[i]

            # print(cmx,cmn)
    return (cmx, cmn)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
