# Reverse bits of a given 32 bits signed integer.

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Shift result to the left to make space for the next bit
            result = (result << 1) | (n & 1)
            n >>= 1
        return result
