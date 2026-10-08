# You are given a string s consisting of lowercase English letters.
#
# Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2
# in the string such that:
#
# a1 has an odd frequency in the string.
# a2 has an even frequency in the string.
# Return this maximum difference.

from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)

        max_odd = max(freq for freq in counts.values() if freq % 2)
        min_even = min(freq for freq in counts.values() if freq % 2 == 0)

        return max_odd - min_even
