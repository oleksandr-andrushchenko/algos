# You are given a string s and two distinct lowercase English letters x and y.
#
# Rearrange the characters of s to construct a new string t such that:
#
# t is a permutation of s.
# Every occurrence of y appears before every occurrence of x in t.
# Return any valid string t.

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        return y * s.count(y) + "".join(char for char in s if char != y)
