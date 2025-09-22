# Jesse loves cookies and wants the sweetness of some cookies to be greater than value .
# To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:
#
# sweetness  Least sweet cookie   2nd least sweet cookie).
#
# This occurs until all the cookies have a sweetness .
#
# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return .


#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq


def cookies(k, a):
    heapq.heapify(a)

    if a[0] >= k:
        return 0

    i = 1
    while a and len(a) > 1:
        s1, s2 = heapq.heappop(a), heapq.heappop(a)
        heapq.heappush(a, s1 + s2 * 2)
        if a[0] >= k:
            return i
        i += 1

    return -1


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
