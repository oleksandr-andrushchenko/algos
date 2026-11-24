# You are given an integer array nums.
#
# Choose exactly one pair of distinct indices i and j. The strength of the pair is defined as
# (nums[i] * nums[j]) / gcd(nums[i], nums[j])2.
#
# Return the maximum strength over all possible pairs.

from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        return max(
            (nums[i] * nums[j]) // (gcd(nums[i], nums[j]) ** 2)
            for i in range(len(nums))
            for j in range(i + 1, len(nums))
        )
