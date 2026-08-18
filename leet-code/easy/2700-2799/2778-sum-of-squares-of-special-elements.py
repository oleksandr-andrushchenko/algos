# You are given a 1-indexed integer array nums of length n.
#
# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
#
# Return the sum of the squares of all special elements of nums.

from typing import List


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        for i, num in enumerate(nums, 1):
            if n % i == 0:
                answer += num * num

        return answer
