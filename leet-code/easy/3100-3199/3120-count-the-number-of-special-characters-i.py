# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
#
# Return the number of special letters in word.

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set(word)

        return sum(char.upper() in chars for char in chars if char.islower())
