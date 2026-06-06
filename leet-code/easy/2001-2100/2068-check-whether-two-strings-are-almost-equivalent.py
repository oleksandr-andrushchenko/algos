# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter
# from 'a' to 'z' between word1 and word2 is at most 3.
#
# Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false
# otherwise.
#
# The frequency of a letter x is the number of times it occurs in the string.

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord('a')] += 1

        for ch in word2:
            freq2[ord(ch) - ord('a')] += 1

        for i in range(26):
            if abs(freq1[i] - freq2[i]) > 3:
                return False

        return True