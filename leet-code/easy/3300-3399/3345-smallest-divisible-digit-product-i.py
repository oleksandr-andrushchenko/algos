# You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its
# digits is divisible by t.

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1

            for digit in str(n):
                product *= int(digit)

            if product % t == 0:
                return n

            n += 1
