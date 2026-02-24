# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
