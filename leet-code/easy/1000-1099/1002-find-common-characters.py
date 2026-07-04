# Given a string array words, return an array of all characters that show up in all strings within the words (including
# duplicates). You may return the answer in any order.

from collections import Counter


class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)  # intersection: keeps min counts

        result = []
        for char, count in common.items():
            result.extend([char] * count)

        return result
