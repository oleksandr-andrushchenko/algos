# You are given a string title consisting of one or more words separated by a single space, where each word consists of
# English letters. Capitalize the string by changing the capitalization of each word such that:
#
# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()

        for i, word in enumerate(words):
            if len(word) <= 2:
                words[i] = word.lower()
            else:
                words[i] = word.capitalize()

        return " ".join(words)
