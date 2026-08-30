# You are given positive integers n and m.
#
# Define two integers as follows:
#
# num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
# num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
# Return the integer num1 - num2.

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = sum(i for i in range(1, n + 1) if i % m != 0)
        num2 = sum(i for i in range(1, n + 1) if i % m == 0)

        return num1 - num2
