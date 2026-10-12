# Given an array nums, you can perform the following operation any number of times:
#
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.
#
# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).


from typing import List


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        while any(nums[i] > nums[i + 1] for i in range(len(nums) - 1)):
            i = min(
                range(len(nums) - 1),
                key=lambda i: nums[i] + nums[i + 1]
            )

            nums[i:i + 2] = [nums[i] + nums[i + 1]]
            operations += 1

        return operations
