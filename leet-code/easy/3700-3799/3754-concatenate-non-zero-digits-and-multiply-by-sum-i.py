# You are given an integer n.
#
# Form a new integer x by concatenating all the non-zero digits of n in their original order. If there are no non-zero
# digits, x = 0.
#
# Let sum be the sum of digits in x.
#
# Return an integer representing the value of x * sum.

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        digits = [int(d) for d in str(n) if d != '0']
        x = int(''.join(map(str, digits))) if digits else 0

        return x * sum(digits)
