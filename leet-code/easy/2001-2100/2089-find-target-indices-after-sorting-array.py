# You are given a 0-indexed integer array nums and a target element target.
#
# A target index is an index i such that nums[i] == target.
#
# Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices,
# return an empty list. The returned list must be sorted in increasing order.

from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = 0
        count = 0

        for num in nums:
            if num < target:
                smaller += 1
            elif num == target:
                count += 1

        return list(range(smaller, smaller + count))
