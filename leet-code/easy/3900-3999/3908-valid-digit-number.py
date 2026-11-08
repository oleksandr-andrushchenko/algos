# You are given an integer n and a digit x.
#
# A number is considered valid if:
#
# It contains at least one occurrence of digit x, and
# It does not start with digit x.
# Return true if n is valid, otherwise return false.

class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        digits = str(abs(n))
        digit = str(x)

        return digit in digits and digits[0] != digit
