# You are given a 0-indexed array nums of integers.
#
# A triplet of indices (i, j, k) is a mountain if:
#
# i < j < k
# nums[i] < nums[j] and nums[k] < nums[j]
# Return the minimum possible sum of a mountain triplet of nums. If no such triplet exists, return -1.

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        left_min = [0] * n
        right_min = [0] * n

        left_min[0] = nums[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], nums[i])

        right_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i])

        ans = float('inf')

        for j in range(1, n - 1):
            if left_min[j - 1] < nums[j] and right_min[j + 1] < nums[j]:
                ans = min(
                    ans,
                    left_min[j - 1] + nums[j] + right_min[j + 1]
                )

        return -1 if ans == float('inf') else ans
