# Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that
# the two subarrays must begin at different indices.
#
# Return true if these subarrays exist, and false otherwise.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List


class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()

        for i in range(len(nums) - 1):
            current_sum = nums[i] + nums[i + 1]

            if current_sum in seen:
                return True

            seen.add(current_sum)

        return False
