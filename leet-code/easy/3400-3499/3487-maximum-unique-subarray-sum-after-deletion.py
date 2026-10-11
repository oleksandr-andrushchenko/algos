# You are given an integer array nums.
#
# You are allowed to delete any number of elements from nums without making it empty. After performing the deletions,
# select a subarray of nums such that:
#
# All elements in the subarray are unique.
# The sum of the elements in the subarray is maximized.
# Return the maximum sum of such a subarray.


from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positives = {num for num in nums if num > 0}

        return sum(positives) if positives else max(nums)
