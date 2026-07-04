# Given a 2D integer array nums where nums[i] is a non-empty array of distinct positive integers, return the list of
# integers that are present in each array of nums sorted in ascending order.

from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = set(nums[0])

        for arr in nums[1:]:
            common &= set(arr)

        return sorted(common)
