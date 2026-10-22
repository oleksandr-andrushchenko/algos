# You are given an integer array nums.
#
# The alternating sum of nums is the value obtained by adding elements at even indices and subtracting elements at odd
# indices. That is, nums[0] - nums[1] + nums[2] - nums[3]...
#
# Return an integer denoting the alternating sum of nums.


from typing import List


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        return sum(num if i % 2 == 0 else -num for i, num in enumerate(nums))
