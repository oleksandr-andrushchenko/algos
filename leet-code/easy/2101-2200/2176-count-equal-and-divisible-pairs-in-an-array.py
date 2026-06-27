# Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) where
# 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.

from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1

        return count
