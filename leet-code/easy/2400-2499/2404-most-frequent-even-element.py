# Given an integer array nums, return the most frequent even element.
#
# If there is a tie, return the smallest one. If there is no such element, return -1.

from typing import List
from collections import Counter


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = Counter(num for num in nums if num % 2 == 0)

        if not count:
            return -1

        ans = -1
        freq = 0

        for num, c in count.items():
            if c > freq or (c == freq and num < ans):
                ans = num
                freq = c

        return ans
