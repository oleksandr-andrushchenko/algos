# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum
# value of (nums[i]-1)*(nums[j]-1).

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max1 = max2 = 0

        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num

        return (max1 - 1) * (max2 - 1)
