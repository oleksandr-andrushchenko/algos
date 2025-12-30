# Given a string licensePlate and an array of strings words, find the shortest completing word in words.
#
# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate,
# and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the
# word the same number of times or more.
#
# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice.
# Possible completing words are "abccdef", "caaacab", and "cbca".
#
# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest
# completing words, return the first one that occurs in words.

from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Count required letters from licensePlate (ignore digits and spaces)
        required = Counter(
            ch.lower() for ch in licensePlate if ch.isalpha()
        )

        shortest_word = None

        for word in words:
            word_count = Counter(word.lower())

            # Check if word satisfies all required letter counts
            is_completing = True
            for letter, count in required.items():
                if word_count[letter] < count:
                    is_completing = False
                    break

            if is_completing:
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word

        return shortest_word
