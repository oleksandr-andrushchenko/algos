# You are given two non-negative integers n and s.
#
# Return the largest integer that has at most n digits and whose sum of digits is s. If no such integer exists, return -1.

class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if n == 0 or s > 9 * n:
            return -1

        if s == 0:
            return 0

        result = 0

        for _ in range(n):
            digit = min(9, s)
            result = result * 10 + digit
            s -= digit

        return result
