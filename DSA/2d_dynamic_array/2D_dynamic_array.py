#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    print()
    # Write your code here
    lastAnswer = 0
    answer_array = []
    arr = [[]for _ in range(n)]
    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]
        
        if query_type == 1:
            idx = ((x ^ lastAnswer) % n)
            arr[idx].append(y)
        else:
            idx = ((x ^ lastAnswer) % n)
            lastAnswer = arr[idx][y % len(arr[idx])]
            answer_array.append(lastAnswer)
        
    return(answer_array)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
