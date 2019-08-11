#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    #absolute diagonal difference
    #11, 22, 33 and 13, 22, 31
    #11,22,33,44 and 14,23, 32, 41
    sum1 = 0;
    sum2 = 0;

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (i==1 and j==1):
                sum1 = sum1 + arr[i][j];
            elif (i == 2 and j==2):
                sum1 = sum1 + arr[i][j];
                sum2 = sum2 + arr[i][j];
            elif (i==3 and j==3):
                sum1 = sum1 + arr[i][j];
            elif (i==1 and j==3) or (i==3 and j==1):
                sum2 = sum2 + arr[i][j];
                #print(arr[i][j])
    print(sum1);
    print(sum2);
    return abs(sum1 - sum2);

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
