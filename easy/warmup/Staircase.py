#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    res_list=list()
    for i in range(n):
        res_list.append(' ')
    for i in range(n):
        res_list.append('#')
        res_list=res_list[1:]
        for i in res_list:
            print(i,end='')
        print()
    
        

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
