# A substring is a contiguous (non-empty) sequence of characters within a string.
#
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels
# present in it.
#
# Given a string word, return the number of vowel substrings in word.

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        result = 0

        for left in range(len(word)):
            seen = set()

            for right in range(left, len(word)):
                if word[right] not in vowels:
                    break

                seen.add(word[right])

                if len(seen) == 5:
                    result += 1

        return result
