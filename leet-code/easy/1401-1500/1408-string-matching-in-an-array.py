# Given an array of string words, return all strings in words that are a substring of another word.
# You can return the answer in any order.

class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]:
                    result.append(words[i])
                    break

        return result
