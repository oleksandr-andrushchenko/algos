# Given an integer array nums containing distinct positive integers, find and return any number from the array that is
# neither the minimum nor the maximum value in the array, or -1 if there is no such number.
#
# Return the selected integer.

from typing import List


class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return -1

        return sorted(nums[:3])[1]
