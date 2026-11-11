# You are given an integer n.
#
# Return true if its binary representation contains exactly one adjacent pair of set bits, and false otherwise.

class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        pairs = n & (n >> 1)
        return pairs > 0 and (pairs & (pairs - 1)) == 0
