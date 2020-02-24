#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #

    ns = s.rstrip('APM').split(':')
    ns[0] = int(ns[0])
    ns[0] = ns[0] % 12
    if 'PM' in s:
        ns[0] += 12
    else:
        ns[0] = str('0' + str(ns[0]))
    ns[0] = str(ns[0])
    ts = ':'.join(ns)

    return ts


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
