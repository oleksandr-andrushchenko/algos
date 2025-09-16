# Your task is to reverse an array of integers.

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # return a[::-1]
    i, j = 0, len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return a


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()[:n]))

    res = reverseArray(arr)

    print(' '.join(map(str, res)))
