# Given a positive integer n, write a function that returns the number of set bits in its binary representation
# (also known as the Hamming weight).

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    def hammingWeight2(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1  # Add 1 if the least significant bit is set
            n >>= 1  # Right-shift n by one bit
        return count
