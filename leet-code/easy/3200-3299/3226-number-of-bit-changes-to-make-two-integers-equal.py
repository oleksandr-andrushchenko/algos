# You are given two positive integers n and k.
#
# You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.
#
# Return the number of changes needed to make n equal to k. If it is impossible, return -1.

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n & k != k:
            return -1

        return (n ^ k).bit_count()
