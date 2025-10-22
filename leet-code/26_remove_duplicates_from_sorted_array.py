# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
# element appears only once. The relative order of the elements should be kept the same.
#
# Consider the number of unique elements in nums to be k.
# After removing duplicates, return the number of unique elements k.
#
# The first k elements of nums should contain the unique numbers in sorted order.
# The remaining elements beyond index k - 1 can be ignored.

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]

        left += 1
        for i in range(left + 1, len(nums)):
            nums[i] = '_'

        return left
