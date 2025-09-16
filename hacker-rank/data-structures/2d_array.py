# Task
#
# Given a  2D array, , an hourglass is a subset of values with indices falling in the following pattern:
#
# a b c
#   d
# e f g
# There are  hourglasses in a  array. The  is the sum of the values in an hourglass.
# Calculate the hourglass sum for every hourglass in , then print the  hourglass sum.

# !/bin/python3

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

def hourglassSum(a):
    max_sum = -float('inf')
    for i in range(4):
        for j in range(4):
            cur_sum = (a[i][j] + a[i][j + 1] + a[i][j + 2]
                       + a[i + 1][j + 1]
                       + a[i + 2][j] + a[i + 2][j + 1] + a[i + 2][j + 2])
            max_sum = max(max_sum, cur_sum)
    return max_sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    print(str(result))
