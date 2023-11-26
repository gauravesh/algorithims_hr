#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    str_list = list(map(str, s.split(':')))
    last=str_list[-1]
    
    if str_list[0] == '12' :
        str_list[0]='00'
    if 'PM' in str_list[-1]:
        str_list[0]=str(int(str_list[0])+12)

    str_list[-1]=last[:2]

    return ':'.join(str_list)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
