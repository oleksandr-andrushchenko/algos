# You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:
#
# Replace each even number with 0.
# Replace each odd numbers with 1.
# Sort the modified array in non-decreasing order.
# Return the resulting array after performing these operations.


from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        ones = sum(num % 2 for num in nums)
        return [0] * (len(nums) - ones) + [1] * ones
