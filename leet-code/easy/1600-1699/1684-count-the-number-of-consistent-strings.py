# You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent
# if all characters in the string appear in the string allowed.
#
# Return the number of consistent strings in the array words.

class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        allowed_set = set(allowed)
        count = 0

        for word in words:
            if all(c in allowed_set for c in word):
                count += 1

        return count
