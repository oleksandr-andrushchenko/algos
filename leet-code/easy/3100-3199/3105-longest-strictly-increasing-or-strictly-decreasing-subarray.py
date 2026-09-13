# You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly
# increasing or strictly decreasing.

from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing = 1
        decreasing = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing += 1
                decreasing = 1
            elif nums[i] < nums[i - 1]:
                decreasing += 1
                increasing = 1
            else:
                increasing = 1
                decreasing = 1

            ans = max(ans, increasing, decreasing)

        return ans
