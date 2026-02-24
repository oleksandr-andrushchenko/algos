# Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation
# of n. If there are no two adjacent 1's, return 0.
#
# Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute
# difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]  # convert to binary string
        prev_index = None
        max_distance = 0

        for i, bit in enumerate(binary):
            if bit == '1':
                if prev_index is not None:
                    max_distance = max(max_distance, i - prev_index)
                prev_index = i

        return max_distance
