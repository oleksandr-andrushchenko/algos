# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number
# of positions (including zero). Otherwise, return false.
#
# There may be duplicates in the original array.
#
# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length]
# for every valid index i.

class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
                if count > 1:
                    return False

        return True
