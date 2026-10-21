# You are given an integer array nums.
#
# Return the smallest absent positive integer in nums such that it is strictly greater than the average of all elements
# in nums.
#
# The average of an array is defined as the sum of all its elements divided by the number of elements.


from typing import List


class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) / len(nums)
        seen = set(nums)

        result = max(1, int(avg) + 1)

        while result in seen:
            result += 1

        return result
