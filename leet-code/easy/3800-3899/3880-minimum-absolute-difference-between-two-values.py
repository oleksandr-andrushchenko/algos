# You are given an integer array nums consisting only of 0, 1, and 2.
#
# A pair of indices (i, j) is called valid if nums[i] == 1 and nums[j] == 2.
#
# Return the minimum absolute difference between i and j among all valid pairs. If no valid pair exists, return -1.
#
# The absolute difference between indices i and j is defined as abs(i - j).

class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        last_one = -1
        last_two = -1
        best = len(nums)

        for i, num in enumerate(nums):
            if num == 1:
                last_one = i
                if last_two != -1:
                    best = min(best, i - last_two)

            elif num == 2:
                last_two = i
                if last_one != -1:
                    best = min(best, i - last_one)

        return best if best < len(nums) else -1
