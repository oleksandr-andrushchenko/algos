# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        l = len(s)
        i = l - 1

        while i >= 0 and s[i] == " ": i -= 1

        while i >= 0 and s[i] != " ":
            res += 1
            i -= 1

        return res
