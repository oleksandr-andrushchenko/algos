# You are given an integer n.
#
# The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two numbers.
# Its first few terms are 0, 1, 1, 2, 3, 5, 8, 13, ....
#
# Return true if n can be expressed as the sum of three consecutive terms in the Fibonacci sequence, and false otherwise.

class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if n < 2 or n % 2 != 0:
            return False

        target = n // 2
        a, b = 0, 1

        while b < target:
            a, b = b, a + b

        return b == target
