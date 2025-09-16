# Task
#
# A  operation on a circular array shifts each of the array's elements  unit to the left.
# The elements that fall off the left end reappear at the right end.
# Given an integer , rotate the array that many steps to the left and return the result.

# Input Format
#
# The first line contains two space-separated integers that denote , the number of integers, and , the number of left rotations to perform.
# The second line contains  space-separated integers that describe .

# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr

from collections import deque


def rotateLeft(d, arr):
    arr_q = deque(arr)
    for _ in range(d):
        arr_q.append(arr_q.popleft())
    return arr_q


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    print(' '.join(map(str, result)))
