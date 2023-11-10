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
    
    len_arr=len(arr)
    rt_diag=[]
    left_diag=[]
    for i in range (len_arr):
        for j in range(len_arr):
            if (i+j)==len_arr-1:
                rt_diag.append(arr[i][j])
            if i==j:
                left_diag.append(arr[i][j])
    return abs(sum(rt_diag)-sum(left_diag))
                
                
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
