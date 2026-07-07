# You are given a string s, where every two consecutive vertical bars '|' are grouped into a pair. In other words, the
# 1st and 2nd '|' make a pair, the 3rd and 4th '|' make a pair, and so forth.
#
# Return the number of '*' in s, excluding the '*' between each pair of '|'.
#
# Note that each '|' will belong to exactly one pair.

class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        inside = False

        for c in s:
            if c == "|":
                inside = not inside
            elif c == "*" and not inside:
                count += 1

        return count
