# Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.
#
# Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.

from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0

        for num in nums:
            if num % 6 == 0:
                total += num
                count += 1

        return total // count if count else 0
