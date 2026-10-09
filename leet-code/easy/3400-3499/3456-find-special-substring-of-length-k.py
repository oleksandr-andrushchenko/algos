# You are given a string s and an integer k.
#
# Determine if there exists a substring of length exactly k in s that satisfies the following conditions:
#
# The substring consists of only one distinct character (e.g., "aaa" or "bbb").
# If there is a character immediately before the substring, it must be different from the character in the substring.
# If there is a character immediately after the substring, it must also be different from the character in the substring.
# Return true if such a substring exists. Otherwise, return false.


class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s) - k + 1):
            if (
                    len(set(s[i:i + k])) == 1
                    and (i == 0 or s[i - 1] != s[i])
                    and (i + k == len(s) or s[i + k] != s[i])
            ):
                return True

        return False
