# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that
# |nums[i] - nums[j]| == k.
#
# The value of |x| is defined as:
#
# x if x >= 0.
# -x if x < 0.

from collections import Counter


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        freq = Counter()

        for num in nums:
            count += freq[num - k]
            count += freq[num + k]
            freq[num] += 1

        return count
