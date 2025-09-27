# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
#
# You must not use any built-in exponent function or operator.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        lo, hi = 1, x // 2  # sqrt(x) <= x//2 for x>=4
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq < x:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi
