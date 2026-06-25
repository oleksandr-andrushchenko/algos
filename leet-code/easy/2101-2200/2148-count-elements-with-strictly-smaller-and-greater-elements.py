# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater
# element appear in nums.

from typing import List


class Solution:
    def countElements(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        count = 0

        for num in nums:
            if smallest < num < largest:
                count += 1

        return count
