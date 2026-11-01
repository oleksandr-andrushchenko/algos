# You are given a string s that consists of lowercase English letters.
#
# Return the string obtained by removing all trailing vowels from s.
#
# The vowels consist of the characters 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        return s.rstrip("aeiou")
