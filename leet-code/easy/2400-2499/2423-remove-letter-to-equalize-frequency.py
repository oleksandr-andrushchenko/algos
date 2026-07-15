# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and
# remove the letter at that index from word so that the frequency of every letter present in word is equal.
#
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false
# otherwise.
#
# Note:
#
# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.

from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        count = Counter(word)

        for ch in count:
            count[ch] -= 1

            if count[ch] == 0:
                del count[ch]

            if len(set(count.values())) == 1:
                return True

            count[ch] = count.get(ch, 0) + 1

        return False
