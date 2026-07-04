# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
#
# Return the largest lucky integer in the array. If there is no lucky integer return -1.

from collections import Counter


class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq = Counter(arr)
        ans = -1

        for num, count in freq.items():
            if num == count:
                ans = max(ans, num)

        return ans
