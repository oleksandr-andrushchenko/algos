# You are given two integer arrays,  and  of dimensions X.
# Your task is to perform the following operations:
#
# Add ( + )
# Subtract ( - )
# Multiply ( * )
# Integer Division ( / )
# Mod ( % )
# Power ( ** )

# Input Format
#
# The first line contains two space separated integers,  and .
# The next  lines contains  space separated integers of array .
# The following  lines contains  space separated integers of array .

import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr_1 = []
    for _ in range(0, n):
        arr_1.append(list(map(int, input().split()))[:m])
    arr_1_np = np.array(arr_1)

    arr_2 = []
    for _ in range(0, n):
        arr_2.append(list(map(int, input().split()))[:m])
    arr_2_np = np.array(arr_2)

    print(arr_1_np + arr_2_np)
    print(arr_1_np - arr_2_np)
    print(arr_1_np * arr_2_np)
    print(arr_1_np // arr_2_np)
    print(arr_1_np % arr_2_np)
    print(arr_1_np ** arr_2_np)
