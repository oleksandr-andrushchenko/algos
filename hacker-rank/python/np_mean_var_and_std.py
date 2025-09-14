# You are given a 2-D array of size X.
# Your task is to find:
#
# The mean along axis
# The var along axis
# The std along axis

# Input Format
#
# The first line contains the space separated values of  and .
# The next  lines contains  space separated integers.

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = [list(map(int, input().split()[:m])) for _ in range(n)]
    np_arr = np.array(arr)

    print(np.mean(np_arr, axis=1))
    print(np.var(np_arr, axis=0))

    std_value = np.std(np_arr)
    if np.isclose(std_value, round(std_value)):
        print(f"{std_value:.1f}")
    else:
        print(f"{std_value:.11f}")
