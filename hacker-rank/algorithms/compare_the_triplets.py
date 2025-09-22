# Alice and Bob each created one problem for HackerRank.
# A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories:
# problem clarity, originality, and difficulty.
#
# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the
# triplet b = (b[0], b[1], b[2]).
#
# The task is to calculate their comparison points by comparing each category:
#
# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    r1, r2 = 0, 0
    for i in range(len(a)):
        if a[i] > b[i]:
            r1 += 1
        elif a[i] < b[i]:
            r2 += 1
    return [r1, r2]


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
