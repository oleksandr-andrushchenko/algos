# You are given two integer arrays of size X and X ( &  are rows, and  is the column).
# Your task is to concatenate the arrays along axis .

# Input Format
#
# The first line contains space separated integers ,  and .
# The next  lines contains the space separated elements of the  columns.
# After that, the next  lines contains the space separated elements of the  columns.

import numpy as np

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    arr_1 = []
    arr_2 = []

    for _ in range(0, n):
        arr_1.append(list(map(int, input().split()))[:p])

    for _ in range(0, m):
        arr_2.append(list(map(int, input().split()))[:p])

    arr_1_np = np.array(arr_1)
    arr_2_np = np.array(arr_2)

    res = np.concatenate((arr_1_np, arr_2_np), axis=0)
    print(res)
