# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        freq = Counter(nums)
        longest = 0

        for num in freq:
            if num + 1 in freq:
                longest = max(longest, freq[num] + freq[num + 1])

        return longest
