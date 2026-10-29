# You are given a string s consisting of lowercase English letters, spaces, and digits.
#
# Let v be the number of vowels in s and c be the number of consonants in s.
#
# A vowel is one of the letters 'a', 'e', 'i', 'o', or 'u', while any other letter in the English alphabet is considered
# a consonant.
#
# The score of the string s is defined as follows:
#
# If c > 0, the score = floor(v / c) where floor denotes rounding down to the nearest integer.
# Otherwise, the score = 0.
# Return an integer denoting the score of the string.

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vowels = set("aeiou")
        v = c = 0

        for char in s:
            if char in vowels:
                v += 1
            elif 'a' <= char <= 'z':
                c += 1

        return v // c if c > 0 else 0
