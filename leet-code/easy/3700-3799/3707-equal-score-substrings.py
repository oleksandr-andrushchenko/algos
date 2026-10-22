# You are given a string s consisting of lowercase English letters.
#
# The score of a string is the sum of the positions of its characters in the alphabet, where 'a' = 1, 'b' = 2, ..., 'z'
# = 26.
#
# Determine whether there exists an index i such that the string can be split into two non-empty substrings s[0..i] and
# s[(i + 1)..(n - 1)] that have equal scores.
#
# Return true if such a split exists, otherwise return false.


class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = sum(ord(c) - ord('a') + 1 for c in s)
        left = 0

        for c in s[:-1]:
            left += ord(c) - ord('a') + 1

            if left * 2 == total:
                return True

        return False
