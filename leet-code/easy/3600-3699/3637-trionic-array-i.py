# You are given an integer array nums of length n.
#
# An array is trionic if there exist indices 0 < p < q < n − 1 such that:
#
# nums[0...p] is strictly increasing,
# nums[p...q] is strictly decreasing,
# nums[q...n − 1] is strictly increasing.
# Return true if nums is trionic, otherwise return false.


from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        if i == 0:
            return False

        p = i

        while i + 1 < n and nums[i] > nums[i + 1]:
            i += 1

        if i == p:
            return False

        q = i

        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1

        return q < n - 1 and i == n - 1
