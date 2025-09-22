# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to .

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

from collections import Counter


def pickingNumbers(a):
    max_len = 0
    freq = Counter(a)

    for n in a:
        cur_len = freq[n] + freq.get(n + 1, 0)
        max_len = max(cur_len, max_len)

    return max_len


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
