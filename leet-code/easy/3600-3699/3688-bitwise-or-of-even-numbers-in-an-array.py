# You are given an integer array nums.
#
# Return the bitwise OR of all even numbers in the array.
#
# If there are no even numbers in nums, return 0.

from typing import List


class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0

        for num in nums:
            if num % 2 == 0:
                result |= num

        return result
