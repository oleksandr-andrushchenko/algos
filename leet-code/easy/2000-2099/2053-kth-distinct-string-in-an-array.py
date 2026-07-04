# A distinct string is a string that is present only once in an array.
#
# Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer
# than k distinct strings, return an empty string "".
#
# Note that the strings are considered in the order in which they appear in the array.

from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)

        for word in arr:
            if counts[word] == 1:
                k -= 1

                if k == 0:
                    return word

        return ""
