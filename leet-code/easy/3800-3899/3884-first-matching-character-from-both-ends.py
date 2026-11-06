# You are given a string s of length n consisting of lowercase English letters.
#
# Return the smallest index i such that s[i] == s[n - i - 1].
#
# If no such index exists, return -1.

class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        n = len(s)

        for i in range((n + 1) // 2):
            if s[i] == s[n - i - 1]:
                return i

        return -1
