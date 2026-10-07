# Given a circular array nums, find the maximum absolute difference between adjacent elements.
#
# Note: In a circular array, the first and last elements are adjacent.

from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)

        return max(
            abs(nums[i] - nums[(i + 1) % n])
            for i in range(n)
        )
