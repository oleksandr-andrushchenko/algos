# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a
# string (not necessarily different) and swap the characters at these indices.
#
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the
# strings. Otherwise, return false.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                if len(diff) > 2:
                    return False

        if len(diff) != 2:
            return False

        i, j = diff
        return s1[i] == s2[j] and s1[j] == s2[i]
