# You are given two integers n and k.
#
# A positive integer x is called compatible if it satisfies both of the following conditions:
#
# abs(n - x) <= k
# (n & x) == 0
# Return the sum of all compatible integers x.
#
# Note:
#
# Here, & denotes the bitwise AND operator.
# The absolute difference between integers i and j is defined as abs(i - j).

class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        return sum(
            x
            for x in range(max(1, n - k), n + k + 1)
            if (n & x) == 0
        )
