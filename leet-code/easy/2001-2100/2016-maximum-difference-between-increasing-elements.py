# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and
# nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
#
# Return the maximum difference. If no such i and j exists, return -1.

from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        answer = -1

        for num in nums[1:]:
            if num > min_so_far:
                answer = max(answer, num - min_so_far)

            min_so_far = min(min_so_far, num)

        return answer
