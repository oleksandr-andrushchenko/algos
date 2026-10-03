# Given an array nums of n integers and an integer k, determine whether there exist two adjacent subarrays of length k
# such that both subarrays are strictly increasing. Specifically, check if there are two subarrays starting at indices a
# and b (a < b), where:
#
# Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
# The subarrays must be adjacent, meaning b = a + k.
# Return true if it is possible to find two such subarrays, and false otherwise.

from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for start in range(len(nums) - 2 * k + 1):
            first = all(
                nums[i] < nums[i + 1]
                for i in range(start, start + k - 1)
            )

            second = all(
                nums[i] < nums[i + 1]
                for i in range(start + k, start + 2 * k - 1)
            )

            if first and second:
                return True

        return False
