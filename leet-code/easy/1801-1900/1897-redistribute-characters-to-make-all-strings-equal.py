# You are given an array of strings words (0-indexed).
#
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from
# words[i] to any position in words[j].
#
# Return true if you can make every string in words equal using any number of operations, and false otherwise.

class Solution:
    def makeEqual(self, words: list[str]) -> bool:
        char_count = {}

        for word in words:
            for char in word:
                char_count[char] = char_count.get(char, 0) + 1

        for count in char_count.values():
            if count % len(words) != 0:
                return False

        return True
