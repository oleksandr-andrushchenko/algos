# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).
#
# Return the sum of lengths of all good strings in words.

from collections import Counter


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0

        for word in words:
            word_count = Counter(word)

            # Check if word can be formed
            if all(word_count[c] <= chars_count[c] for c in word_count):
                total_length += len(word)

        return total_length
