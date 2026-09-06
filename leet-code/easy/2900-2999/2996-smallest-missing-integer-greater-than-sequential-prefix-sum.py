# You are given a 0-indexed array of integers nums.
#
# A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix
# consisting only of nums[0] is sequential.
#
# Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest
# sequential prefix.

from typing import List


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            total += nums[i]

        seen = set(nums)

        while total in seen:
            total += 1

        return total
