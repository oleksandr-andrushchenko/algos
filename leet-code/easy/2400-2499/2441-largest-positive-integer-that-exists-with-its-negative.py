# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also
# exists in the array.
#
# Return the positive integer k. If there is no such integer, return -1.

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set(nums)
        answer = -1

        for num in nums:
            if num > 0 and -num in seen:
                answer = max(answer, num)

        return answer
