# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for v in nums:
            idx = abs(v) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        result = []
        for i, v in enumerate(nums):
            if v > 0:
                result.append(i + 1)

        return result
