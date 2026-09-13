# You are given an array nums of non-negative integers and an integer k.
#
# An array is called special if the bitwise OR of all of its elements is at least k.
#
# Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

from typing import List


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = len(nums) + 1

        for left in range(len(nums)):
            current_or = 0

            for right in range(left, len(nums)):
                current_or |= nums[right]

                if current_or >= k:
                    ans = min(ans, right - left + 1)
                    break

        return ans if ans <= len(nums) else -1
