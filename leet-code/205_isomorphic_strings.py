# Given two strings s and t, determine if they are isomorphic.
#
# Two strings s and t are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character, but a character may map to itself.

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t = {}
        t_to_s = {}

        for ch_s, ch_t in zip(s, t):
            # If mapping already exists, it must match
            if ch_s in s_to_t and s_to_t[ch_s] != ch_t:
                return False
            if ch_t in t_to_s and t_to_s[ch_t] != ch_s:
                return False

            # Create both-direction mapping
            s_to_t[ch_s] = ch_t
            t_to_s[ch_t] = ch_s

        return True
