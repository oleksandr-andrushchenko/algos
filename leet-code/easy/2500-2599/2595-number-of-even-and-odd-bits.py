# You are given a positive integer n.
#
# Let even denote the number of even indices in the binary representation of n with value 1.
#
# Let odd denote the number of odd indices in the binary representation of n with value 1.
#
# Note that bits are indexed from right to left in the binary representation of a number.
#
# Return the array [even, odd].

from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odd = 0
        index = 0

        while n:
            if n & 1:
                if index % 2 == 0:
                    even += 1
                else:
                    odd += 1

            n >>= 1
            index += 1

        return [even, odd]
