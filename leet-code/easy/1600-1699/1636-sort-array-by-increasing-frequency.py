# Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
# If multiple values have the same frequency, sort them in decreasing order.
#
# Return the sorted array.

from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        freq = Counter(nums)

        return sorted(nums, key=lambda x: (freq[x], -x))
