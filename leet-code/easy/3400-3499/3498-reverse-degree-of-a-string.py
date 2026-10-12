# Given a string s, calculate its reverse degree.
#
# The reverse degree is calculated as follows:
#
# For each character, multiply its position in the reversed alphabet ('a' = 26, 'b' = 25, ..., 'z' = 1) with its
# position in the string (1-indexed).
# Sum these products for all characters in the string.
# Return the reverse degree of s.


class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((123 - ord(c)) * i for i, c in enumerate(s, 1))
