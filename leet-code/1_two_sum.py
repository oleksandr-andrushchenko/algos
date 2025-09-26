# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_sums = {}

        for i in range(len(nums)):
            if nums[i] in diff_sums:
                return [i, diff_sums[nums[i]]]

            diff_sums[target - nums[i]] = i
