# You are given a positive integer array nums.
#
# The element sum is the sum of all the elements in nums.
# The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
# Return the absolute difference between the element sum and digit sum of nums.
#
# Note that the absolute difference between two integers x and y is defined as |x - y|.

from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0

        for num in nums:
            while num:
                digit_sum += num % 10
                num //= 10

        return abs(element_sum - digit_sum)
