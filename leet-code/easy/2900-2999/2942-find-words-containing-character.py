# You are given a 0-indexed array of strings words and a character x.
#
# Return an array of indices representing the words that contain the character x.
#
# Note that the returned array may be in any order.

from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]
