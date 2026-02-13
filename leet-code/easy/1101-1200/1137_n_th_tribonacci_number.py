# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1

        a, b, c = 0, 1, 1  # T0, T1, T2

        for _ in range(3, n + 1):
            a, b, c = b, c, a + b + c

        return c
