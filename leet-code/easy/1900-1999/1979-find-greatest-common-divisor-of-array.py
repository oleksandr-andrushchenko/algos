# Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
#
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

class Solution:
    def findGCD(self, nums: list[int]) -> int:
        a, b = min(nums), max(nums)

        while b:
            a, b = b, a % b

        return a
