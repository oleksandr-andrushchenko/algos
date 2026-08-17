# You are given a 0-indexed array words consisting of distinct strings.
#
# The string words[i] can be paired with the string words[j] if:
#
# The string words[i] is equal to the reversed string of words[j].
# 0 <= i < j < words.length.
# Return the maximum number of pairs that can be formed from the array words.
#
# Note that each string can belong in at most one pair.

from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        seen = set()
        answer = 0

        for word in words:
            if word[::-1] in seen:
                answer += 1
            else:
                seen.add(word)

        return answer
