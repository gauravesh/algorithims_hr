#!/bin/python3

import math
import os
import random
import re
import sys


def selection_sort(a):
    sample = a.copy()
    sorted_list = []
    
    while sample:
        min_val = min(sample)
        sorted_list.append(min_val)
        sample.remove(min_val)

    return sorted_list


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    max_val=sum(arr[1:])
    min_val=sum(arr[:-1])
    print(min_val,max_val )

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))
    arr=selection_sort(arr)

    miniMaxSum(arr)
