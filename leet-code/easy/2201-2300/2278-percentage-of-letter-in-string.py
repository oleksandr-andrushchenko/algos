# Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to
# the nearest whole percent.

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return s.count(letter) * 100 // len(s)
