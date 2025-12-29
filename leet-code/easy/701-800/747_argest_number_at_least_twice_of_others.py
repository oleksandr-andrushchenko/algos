# You are given an integer array nums where the largest integer is unique.
#
# Determine whether the largest element in the array is at least twice as much as every other number in the array.
# If it is, return the index of the largest element, or return -1 otherwise.

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max1 = -1
        max2 = -1
        idx = -1

        for i, n in enumerate(nums):
            if n > max1:
                max2 = max1
                max1 = n
                idx = i
            elif n > max2:
                max2 = n

        return idx if max1 >= 2 * max2 else -1
