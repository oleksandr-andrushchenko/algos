# You are given an integer array nums.
#
# You replace each element in nums with the sum of its digits.
#
# Return the minimum element in nums after all replacements.

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(
            sum(map(int, str(num)))
            for num in nums
        )
