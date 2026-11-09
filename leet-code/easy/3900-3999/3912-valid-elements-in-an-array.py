# You are given an integer array nums.
#
# An element nums[i] is considered valid if it satisfies at least one of the following conditions:
#
# It is strictly greater than every element to its left.
# It is strictly greater than every element to its right.
# The first and last elements are always valid.
#
# Return an array of all valid elements in the same order as they appear in nums.

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        valid = [False] * n

        # Elements strictly greater than everything to their left.
        largest = float("-inf")
        for i in range(n):
            if nums[i] > largest:
                valid[i] = True
                largest = nums[i]

        # Elements strictly greater than everything to their right.
        largest = float("-inf")
        for i in range(n - 1, -1, -1):
            if nums[i] > largest:
                valid[i] = True
                largest = nums[i]

        return [num for i, num in enumerate(nums) if valid[i]]
