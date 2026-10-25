# You are given an integer array nums.
#
# In one move, you may increase the value of any single element nums[i] by 1.
#
# Return the minimum total number of moves required so that all elements in nums become equal.

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return max(nums) * len(nums) - sum(nums)
