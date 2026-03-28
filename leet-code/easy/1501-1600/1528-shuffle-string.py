# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the
# character at the ith position moves to indices[i] in the shuffled string.
#
# Return the shuffled string.

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = [''] * len(s)

        for i, ch in enumerate(s):
            res[indices[i]] = ch

        return ''.join(res)
