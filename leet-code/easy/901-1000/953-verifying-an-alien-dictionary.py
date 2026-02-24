# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
#
# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the
# given words are sorted lexicographically in this alien language.

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Map each character to its position in the alien alphabet
        rank = {char: i for i, char in enumerate(order)}

        # Compare each adjacent pair of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]

            # Compare characters
            for c1, c2 in zip(w1, w2):
                if rank[c1] < rank[c2]:
                    break
                if rank[c1] > rank[c2]:
                    return False
            else:
                # All characters matched up to the shorter word
                # Longer word should not come first
                if len(w1) > len(w2):
                    return False

        return True
