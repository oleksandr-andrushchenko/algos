# You are given a string s of length n and an integer k.
#
# A cyclic rotation of s is obtained by choosing a prefix of s whose length is between 0 and n - 1 (inclusive), and
# moving it to the end of the string while preserving the order of all characters.
#
# For every cyclic rotation of s, let its score be the number of indices i such that 0 <= i < n - 1 and the characters
# at positions i and i + 1 are equal.
#
# Return the number of cyclic rotations of s whose score equals k.

class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n = len(s)
        equal_pairs = sum(
            s[i] == s[(i + 1) % n] for i in range(n)
        )

        if k == equal_pairs - 1:
            return equal_pairs
        if k == equal_pairs:
            return n - equal_pairs

        return 0
