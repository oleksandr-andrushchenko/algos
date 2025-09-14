# You are given the shape of the array in the form of space-separated integers,
# each integer representing the size of different dimensions,
# your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

# Input Format
#
# A single line containing the space-separated integers.

import numpy as np

if __name__ == '__main__':
    shape = tuple(map(int, input().split()))

    print(np.zeros(shape, dtype=np.int8))
    print(np.ones(shape, dtype=np.int8))