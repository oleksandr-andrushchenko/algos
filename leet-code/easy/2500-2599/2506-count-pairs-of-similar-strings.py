# You are given a 0-indexed string array words.
#
# Two strings are similar if they consist of the same characters.
#
# For example, "abca" and "cba" are similar since both consist of characters 'a', 'b', and 'c'.
# However, "abacba" and "bcfd" are not similar since they do not consist of the same characters.
# Return the number of pairs (i, j) such that 0 <= i < j <= word.length - 1 and the two strings words[i] and words[j]
# are similar.

from collections import defaultdict
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counts = defaultdict(int)
        answer = 0

        for word in words:
            signature = frozenset(word)
            answer += counts[signature]
            counts[signature] += 1

        return answer
