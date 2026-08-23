# Given a 0-indexed integer array nums of length n and an integer target, return the number of pairs (i, j) where
# 0 <= i < j < n and nums[i] + nums[j] < target.

from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        answer = 0

        while left < right:
            if nums[left] + nums[right] < target:
                answer += right - left
                left += 1
            else:
                right -= 1

        return answer
