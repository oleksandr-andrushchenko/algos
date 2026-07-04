# Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in
# the string. Otherwise, return false.

class Solution:
    def checkString(self, s: str) -> bool:
        return "ba" not in s
