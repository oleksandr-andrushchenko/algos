# Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present
# in at least two out of the three arrays. You may return the values in any order.

from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)

        return [
            num
            for num in s1 | s2 | s3
            if (num in s1) + (num in s2) + (num in s3) >= 2
        ]
