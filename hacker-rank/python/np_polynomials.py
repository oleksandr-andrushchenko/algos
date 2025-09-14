# You are given the coefficients of a polynomial .
# Your task is to find the value of  at point .


# Input Format
#
# The first line contains the space separated value of the coefficients in .
# The second line contains the value of .

import numpy as np

if __name__ == '__main__':
    coeff = list(map(float, input().split()))
    x = float(input())
    res = np.polyval(coeff, x)
    print(res)
