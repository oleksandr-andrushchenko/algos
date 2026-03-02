# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
#
# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.
#
# The test cases are generated so that a unique mapping will always exist.

class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == '#':
                num = int(s[i - 2:i])
                result.append(chr(ord('a') + num - 1))
                i -= 3
            else:
                num = int(s[i])
                result.append(chr(ord('a') + num - 1))
                i -= 1

        return ''.join(reversed(result))
