# A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of
# length n where:
#
# s[i] == 'I' if perm[i] < perm[i + 1], and
# s[i] == 'D' if perm[i] > perm[i + 1].
# Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm,
# return any of them.

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        low, high = 0, n
        perm = []

        for char in s:
            if char == 'I':
                perm.append(low)
                low += 1
            else:  # 'D'
                perm.append(high)
                high -= 1

        # Append the last remaining number
        perm.append(low)  # low == high here
        return perm
