# You are given an integer array nums.
#
# Choose three elements a, b, and c from nums at distinct indices such that the value of the expression a + b - c is
# maximized.
#
# Return an integer denoting the maximum possible value of this expression.

from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] + nums[-2] - nums[0]
