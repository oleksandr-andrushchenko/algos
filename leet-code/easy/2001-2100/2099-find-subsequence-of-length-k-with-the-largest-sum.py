# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the
# largest sum.
#
# Return any such subsequence as an integer array of length k.
#
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the
# order of the remaining elements.

from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed = [(num, i) for i, num in enumerate(nums)]

        # Take k largest elements by value
        largest = sorted(indexed, key=lambda x: x[0], reverse=True)[:k]

        # Sort selected elements by original index to preserve subsequence order
        largest.sort(key=lambda x: x[1])

        return [num for num, _ in largest]
