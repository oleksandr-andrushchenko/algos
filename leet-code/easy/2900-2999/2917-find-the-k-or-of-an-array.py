# You are given an integer array nums, and an integer k. Let's introduce K-or operation by extending the standard
# bitwise OR. In K-or, a bit position in the result is set to 1 if at least k numbers in nums have a 1 in that position.
#
# Return the K-or of nums.

from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        ans = 0

        for bit in range(32):
            count = 0

            for num in nums:
                if num & (1 << bit):
                    count += 1

            if count >= k:
                ans |= 1 << bit

        return ans
