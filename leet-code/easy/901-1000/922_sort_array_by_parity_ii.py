# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
#
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
#
# Return any answer array that satisfies this condition.

class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        i, j = 0, 1
        n = len(nums)

        while i < n and j < n:
            if nums[i] % 2 == 0:
                i += 2
            elif nums[j] % 2 == 1:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2

        return nums
