# You are given an integer array nums.
#
# Consider all pairs of distinct values x and y from nums such that:
#
# x < y
# x and y have different frequencies in nums.
# Among all such pairs:
#
# Choose the pair with the smallest possible value of x.
# If multiple pairs have the same x, choose the one with the smallest possible value of y.
# Return an integer array [x, y]. If no valid pair exists, return [-1, -1].

from collections import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)
        values = sorted(freq)

        for i, x in enumerate(values):
            for y in values[i + 1:]:
                if freq[x] != freq[y]:
                    return [x, y]

        return [-1, -1]
