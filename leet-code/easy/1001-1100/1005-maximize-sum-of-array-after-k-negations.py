# Given an integer array nums and an integer k, modify the array in the following way:
#
# choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the same index i multiple times.
#
# Return the largest possible sum of the array after modifying it in this way.

class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        nums.sort()
        i = 0

        # Flip negative numbers while we can
        while i < len(nums) and nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1

        # If k is still odd, flip the smallest value
        if k % 2 == 1:
            nums.sort()
            nums[0] = -nums[0]

        return sum(nums)
