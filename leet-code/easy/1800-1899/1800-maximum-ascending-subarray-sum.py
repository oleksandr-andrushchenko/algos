# Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.
#
# A subarray is defined as a contiguous sequence of numbers in an array.

class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            max_sum = max(max_sum, current_sum)

        return max_sum
