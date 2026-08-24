# You are given a 0-indexed integer array nums.
#
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a
# negative value, return 0.
#
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        max_left = nums[0]
        max_diff = 0

        for k in range(1, len(nums)):
            result = max(result, max_diff * nums[k])
            max_diff = max(max_diff, max_left - nums[k])
            max_left = max(max_left, nums[k])

        return result
