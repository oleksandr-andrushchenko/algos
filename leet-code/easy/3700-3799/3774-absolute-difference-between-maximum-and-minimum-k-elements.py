# You are given an integer array nums and an integer k.
#
# Find the absolute difference between:
#
# the sum of the k largest elements in the array; and
# the sum of the k smallest elements in the array.
# Return an integer denoting this difference.

from typing import List


class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return abs(sum(nums[-k:]) - sum(nums[:k]))
