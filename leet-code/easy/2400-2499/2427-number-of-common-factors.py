# Given two positive integers a and b, return the number of common factors of a and b.
#
# An integer x is a common factor of a and b if x divides both a and b.

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0

        for x in range(1, min(a, b) + 1):
            if a % x == 0 and b % x == 0:
                ans += 1

        return ans
