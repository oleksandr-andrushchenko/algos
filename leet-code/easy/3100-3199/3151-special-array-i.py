# An array is considered special if the parity of every pair of adjacent elements is different. In other words, one
# element in each pair must be even, and the other must be odd.
#
# You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                return False

        return True
