# You are given a 1-D array, . Your task is to print the ,  and  of all the elements of .

# Input Format
#
# A single line of input containing the space separated elements of array .

import numpy as np

np.set_printoptions(legacy="1.13")

if __name__ == '__main__':
    arr = list(map(float, input().split()))
    arr_np = np.array(arr)

    print(np.floor(arr_np))
    print(np.ceil(arr_np))
    print(np.rint(arr_np))
