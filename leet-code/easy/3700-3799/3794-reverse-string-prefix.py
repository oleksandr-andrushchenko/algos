# You are given a string s and an integer k.
#
# Reverse the first k characters of s and return the resulting string.

class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]
