# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of
# American keyboard like the image below.
#
# Note that the strings are case-insensitive, both lowercased and uppercased of the same letter are treated as if they
# are at the same row.
#
# In the American keyboard:
#
# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res = []
        for w in words:
            lower = set(w.lower())
            if lower <= row1 or lower <= row2 or lower <= row3:
                res.append(w)

        return res
