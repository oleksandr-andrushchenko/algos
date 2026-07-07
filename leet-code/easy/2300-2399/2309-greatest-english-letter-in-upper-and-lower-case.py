# Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase
# letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
#
# An English letter b is greater than another letter a if b appears after a in the English alphabet.

class Solution:
    def greatestLetter(self, s: str) -> str:
        chars = set(s)

        for c in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(c)
            lower = chr(c + 32)

            if upper in chars and lower in chars:
                return upper

        return ""
