# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

from typing import List


class Solution:
    def missingNumber2(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) + 1):
            if i not in nums or nums[i] != i:
                return i
        return -1

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    def missingNumber3(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        for i in range(n + 1):
            xor ^= i
        for num in nums:
            xor ^= num
        return xor
