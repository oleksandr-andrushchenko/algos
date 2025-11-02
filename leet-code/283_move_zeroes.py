# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastN_non_zero_found_at = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastN_non_zero_found_at], nums[i] = nums[i], nums[lastN_non_zero_found_at]
                lastN_non_zero_found_at += 1
