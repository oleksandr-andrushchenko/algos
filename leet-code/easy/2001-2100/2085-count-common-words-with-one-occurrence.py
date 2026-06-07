# Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two
# arrays.

from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count1 = Counter(words1)
        count2 = Counter(words2)

        result = 0

        for word in count1:
            if count1[word] == 1 and count2[word] == 1:
                result += 1

        return result
