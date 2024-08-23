#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    result = []
    for item in operations:
        temp = []
        for new in item.split():
            temp.append(int(new))
        result.append(temp)
        
    answer = []
    output = []

    for element in result:

        if element[0] == 1:
            answer.append(element[1])
    
        elif element[0] == 2:
            answer.pop()

        elif element[0] == 3:
            output.append(max(answer))
        
    return(output)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
''
