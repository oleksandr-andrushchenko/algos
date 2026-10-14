# You are given a string s consisting of lowercase English letters, and an integer k.
#
# Your task is to delete some (possibly none) of the characters in the string so that the number of distinct characters
# in the resulting string is at most k.
#
# Return the minimum number of deletions required to achieve this.


from collections import Counter


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        counts = sorted(Counter(s).values(), reverse=True)
        return sum(counts[k:])
