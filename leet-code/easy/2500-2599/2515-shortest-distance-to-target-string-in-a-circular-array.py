# You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end
# connects to the array's beginning.
#
# Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is
# words[(i - 1 + n) % n], where n is the length of words.
# Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.
#
# Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.

from typing import List


class Solution:
    def closestTarget(
            self,
            words: List[str],
            target: str,
            startIndex: int
    ) -> int:
        n = len(words)
        answer = n

        for i, word in enumerate(words):
            if word == target:
                distance = abs(i - startIndex)
                answer = min(answer, distance, n - distance)

        return answer if answer < n else -1
