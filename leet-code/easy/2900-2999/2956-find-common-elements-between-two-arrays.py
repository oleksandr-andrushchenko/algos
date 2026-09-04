# You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:
#
# answer1 : the number of indices i such that nums1[i] exists in nums2.
# answer2 : the number of indices i such that nums2[i] exists in nums1.
# Return [answer1,answer2].

from typing import List


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        answer1 = sum(num in set2 for num in nums1)
        answer2 = sum(num in set1 for num in nums2)

        return [answer1, answer2]
