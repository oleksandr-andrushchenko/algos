# Given an array of integers nums, you start with an initial positive value startValue.
#
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        current_sum = 0
        min_sum = 0

        for num in nums:
            current_sum += num
            min_sum = min(min_sum, current_sum)

        return 1 - min_sum
