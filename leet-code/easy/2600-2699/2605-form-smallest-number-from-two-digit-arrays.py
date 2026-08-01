# Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from
# each array.

from typing import List


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        common = set(nums1) & set(nums2)

        if common:
            return min(common)

        a = min(nums1)
        b = min(nums2)

        return min(a * 10 + b, b * 10 + a)
