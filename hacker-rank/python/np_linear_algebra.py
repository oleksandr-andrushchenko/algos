# You are given a square matrix  with dimensions X.
# Your task is to find the determinant.
# Note: Round the answer to 2 places after the decimal.

# Input Format
#
# The first line contains the integer .
# The next  lines contains the  space separated elements of array .

import numpy as np

if __name__ == '__main__':
    x = int(input())
    matrix = []
    for _ in range(0, x):
        matrix.append(list(map(float, input().split())))

    res = np.linalg.det(matrix)
    print(round(res, 2))
