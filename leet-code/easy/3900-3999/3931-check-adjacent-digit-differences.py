# You are given a string s consisting of digits.
#
# Return true if the absolute difference between every pair of adjacent digits is at most 2, otherwise return false.
#
# The absolute difference between a and b is defined as abs(a - b).

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        return all(
            abs(int(s[i]) - int(s[i - 1])) <= 2
            for i in range(1, len(s))
        )
