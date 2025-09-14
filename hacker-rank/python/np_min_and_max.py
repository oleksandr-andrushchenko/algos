# You are given a 2-D array with dimensions X.
# Your task is to perform the min function over axis  and then find the max of that.

# The first line of input contains the space separated values of  and .
# The next  lines contains  space separated integers.

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = []
    for _ in range(0, n):
        arr.append(list(map(int, input().split()))[:m])
    np_arr = np.array(arr)

    res = np.max(np.min(np_arr, axis=1))
    print(res)
