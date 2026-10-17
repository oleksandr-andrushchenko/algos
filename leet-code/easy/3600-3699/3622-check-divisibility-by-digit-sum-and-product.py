# You are given a positive integer n. Determine whether n is divisible by the sum of the following two values:
#
# The digit sum of n (the sum of its digits).
#
# The digit product of n (the product of its digits).
#
# Return true if n is divisible by this sum; otherwise, return false.


from math import prod


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits = [int(d) for d in str(n)]
        return n % (sum(digits) + prod(digits)) == 0
