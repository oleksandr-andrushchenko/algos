# You are given a string s consisting only of digits. A valid pair is defined as two adjacent digits in s such that:
#
# The first digit is not equal to the second.
# Each digit in the pair appears in s exactly as many times as its numeric value.
# Return the first valid pair found in the string s when traversing from left to right. If no valid pair exists, return
# an empty string.

from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        counts = Counter(s)

        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]

            if a != b and counts[a] == int(a) and counts[b] == int(b):
                return a + b

        return ""
