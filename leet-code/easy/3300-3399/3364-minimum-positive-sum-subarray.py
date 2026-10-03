# You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose
# size is between l and r (inclusive) and whose sum is greater than 0.
#
# Return the minimum sum of such a subarray. If no such subarray exists, return -1.
#
# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        result = float("inf")

        for i in range(len(nums)):
            total = 0

            for j in range(i, min(i + r, len(nums))):
                total += nums[j]

                if j - i + 1 >= l and total > 0:
                    result = min(result, total)

        return result if result != float("inf") else -1
