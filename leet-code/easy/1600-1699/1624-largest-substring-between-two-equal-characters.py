# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters.
# If there is no such substring return -1.
#
# A substring is a contiguous sequence of characters within a string.

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_seen = {}
        max_len = -1

        for i, ch in enumerate(s):
            if ch in first_seen:
                max_len = max(max_len, i - first_seen[ch] - 1)
            else:
                first_seen[ch] = i

        return max_len
