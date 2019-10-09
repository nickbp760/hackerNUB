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
    i=0; jumlahsatu=0; jumlahdua=0;
    for x in arr:
       jumlahsatu=jumlahsatu+x[i]
       i=i+1
    i=i-1
    for x in arr:
       jumlahdua=jumlahdua+x[i]
       i=i-1

    jumlah=jumlahsatu-jumlahdua

    if(jumlah<0):
        jumlah=jumlah*-1
    return(jumlah)
 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
