# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the
# number of negative integers.
#
# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then
# return the maximum of pos and neg.
# Note that 0 is neither positive nor negative.

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negatives = bisect_left(nums, 0)
        positives = len(nums) - bisect_right(nums, 0)

        return max(negatives, positives)
