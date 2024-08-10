#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    value_2 = []
    for i in range(4):
        for j in range(4):
            value = 0
            for k in range(3):
                for l in range(3):
                    value += (arr[k + i][l + j])
            value_1 = (value - ((arr[1 + i][0 + j]) + (arr[1 + i][2 + j])))
            value_2.append(value_1)
    #print(value_2)
    return(max(value_2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
