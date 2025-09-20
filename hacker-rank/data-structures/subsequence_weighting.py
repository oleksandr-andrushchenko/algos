# A subsequence of a sequence is a sequence which is obtained by deleting zero or more elements from the sequence.
#
# You are given a sequence A in which every element is a pair of integers  i.e  A = [(a1, w1), (a2, w2),..., (aN, wN)].
#
# For a subseqence B = [(b1, v1), (b2, v2), ...., (bM, vM)] of the given sequence :
#
# We call it increasing if for every i (1 <= i < M ) , bi < bi+1.
# Weight(B) = v1 + v2 + ... + vM.
# Task:
# Given a sequence, output the maximum weight formed by an increasing subsequence.

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY w
#

class Fenwick:
    def __init__(self, size):
        self.n = size
        self.bit = [0] * (size + 1)

    def update(self, idx, value):
        while idx <= self.n:
            if value > self.bit[idx]:
                self.bit[idx] = value
            idx += idx & -idx

    def query(self, idx):
        result = 0
        while idx > 0:
            if self.bit[idx] > result:
                result = self.bit[idx]
            idx -= idx & -idx
        return result


def solve(a, w):
    # Coordinate compression: map values of a to smaller indices
    sorted_unique = sorted(set(a))
    compress = {v: i + 1 for i, v in enumerate(sorted_unique)}  # 1-based indexing

    fenwick = Fenwick(len(sorted_unique))
    max_weight = 0

    for value, weight in zip(a, w):
        idx = compress[value]
        # Best weight for subsequences ending with smaller values
        best_before = fenwick.query(idx - 1)
        current = best_before + weight
        fenwick.update(idx, current)
        if current > max_weight:
            max_weight = current

    return max_weight


if __name__ == '__main__':
    fptr = open('tmp.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        a = list(map(int, input().rstrip().split()))
        w = list(map(int, input().rstrip().split()))

        result = solve(a, w)
        fptr.write(str(result) + '\n')

    fptr.close()
