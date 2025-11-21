# Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_count = 0
        current = 0

        for n in nums:
            if n == 1:
                current += 1
                max_count = max(max_count, current)
            else:
                current = 0

        return max_count
