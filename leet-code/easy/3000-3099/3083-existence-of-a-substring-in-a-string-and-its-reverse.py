# Given a string s, find any substring of length 2 which is also present in the reverse of s.
#
# Return true if such a substring exists, and false otherwise.

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        pairs = {s[i:i + 2] for i in range(len(s) - 1)}

        return any(pair[::-1] in pairs for pair in pairs)
