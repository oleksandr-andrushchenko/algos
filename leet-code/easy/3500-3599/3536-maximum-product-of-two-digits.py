# You are given a positive integer n.
#
# Return the maximum product of any two digits in n.
#
# Note: You may use the same digit twice if it appears more than once in n.


class Solution:
    def maxProduct(self, n: int) -> int:
        digits = sorted(map(int, str(n)), reverse=True)
        return digits[0] * digits[1]
