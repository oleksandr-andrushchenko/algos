# You are given a positive integer n.
#
# Let s be the binary representation of n without leading zeros.
#
# The reverse of a binary string s is obtained by writing the characters of s in the opposite order.
#
# You may flip any bit in s (change 0 → 1 or 1 → 0). Each flip affects exactly one bit.
#
# Return the minimum number of flips required to make s equal to the reverse of its original form.

class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]
        return sum(a != b for a, b in zip(s, s[::-1]))
