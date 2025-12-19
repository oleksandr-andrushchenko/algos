# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray).
# The subsequence must be strictly increasing.
#
# A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is
# [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_len = 1
        curr_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr_len += 1
            else:
                curr_len = 1

            max_len = max(max_len, curr_len)

        return max_len
