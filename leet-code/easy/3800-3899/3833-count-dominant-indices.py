# You are given an integer array nums of length n.
#
# An element at index i is called dominant if: nums[i] > average(nums[i + 1], nums[i + 2], ..., nums[n - 1])
#
# Your task is to count the number of indices i that are dominant.
#
# The average of a set of numbers is the value obtained by adding all the numbers together and dividing the sum by the
# total number of numbers.
#
# Note: The rightmost element of any array is not dominant.

from typing import List


class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_sum = 0
        count = 0

        for i in range(n - 1, -1, -1):
            if i < n - 1 and nums[i] * (n - i - 1) > suffix_sum:
                count += 1

            suffix_sum += nums[i]

        return count
