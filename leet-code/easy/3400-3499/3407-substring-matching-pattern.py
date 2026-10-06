# You are given a string s and a pattern string p, where p contains exactly one '*' character.
#
# The '*' in p can be replaced with any sequence of zero or more characters.
#
# Return true if p can be made a substring of s, and false otherwise.

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        prefix, suffix = p.split("*")

        start = s.find(prefix)

        if start == -1:
            return False

        return s.find(suffix, start + len(prefix)) != -1
