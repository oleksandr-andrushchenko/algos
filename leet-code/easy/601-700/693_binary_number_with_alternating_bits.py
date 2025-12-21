# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)
        return (x & (x + 1)) == 0
