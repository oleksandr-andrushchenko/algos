# Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
#
# An integer m is a divisor of n if there exists an integer k such that n = k * m.

import math


class Solution:
    def isThree(self, n: int) -> bool:
        root = int(math.isqrt(n))

        if root * root != n:
            return False

        for i in range(2, int(math.isqrt(root)) + 1):
            if root % i == 0:
                return False

        return root > 1
