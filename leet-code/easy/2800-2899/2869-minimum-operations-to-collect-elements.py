# You are given an array nums of positive integers and an integer k.
#
# In one operation, you can remove the last element of the array and add it to your collection.
#
# Return the minimum number of operations needed to collect elements 1, 2, ..., k.

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collected = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= k:
                collected.add(nums[i])

            if len(collected) == k:
                return len(nums) - i

        return len(nums)
