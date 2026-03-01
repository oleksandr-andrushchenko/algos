# Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        count = 0

        for n in nums:
            if len(str(abs(n))) % 2 == 0:
                count += 1

        return count
