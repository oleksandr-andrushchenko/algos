# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
# For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
# appears, but 'B' does not.
#
# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the
# earliest occurrence. If there are none, return an empty string.

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        char_set = set(s)

        for i, c in enumerate(s):
            if c.swapcase() not in char_set:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i + 1:])
                return left if len(left) >= len(right) else right

        return s
