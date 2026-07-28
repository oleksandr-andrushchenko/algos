# You are given an integer array nums.
#
# The low score of nums is the minimum absolute difference between any two integers.
# The high score of nums is the maximum absolute difference between any two integers.
# The score of nums is the sum of the high and low scores.
# Return the minimum score after changing two elements of nums.

from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()

        return min(
            nums[-1] - nums[2],
            nums[-2] - nums[1],
            nums[-3] - nums[0]
        )
