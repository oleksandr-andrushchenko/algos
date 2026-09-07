# You are given an array nums consisting of positive integers.
#
# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.
#
# The frequency of an element is the number of occurrences of that element in the array.

from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_frequency = max(counts.values())

        return sum(
            frequency
            for frequency in counts.values()
            if frequency == max_frequency
        )
