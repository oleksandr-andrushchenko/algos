# Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one
# element, or false otherwise. If the array is already strictly increasing, return true.
#
# The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        removed = 0

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                removed += 1

                if removed > 1:
                    return False

                if i > 1 and nums[i] <= nums[i - 2]:
                    nums[i] = nums[i - 1]

        return True
