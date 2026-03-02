# Given an integer n, return any array containing n unique integers such that they add up to 0.

class Solution:
    def sumZero(self, n: int) -> list[int]:
        result = []

        # Add symmetric pairs
        for i in range(1, n // 2 + 1):
            result.append(i)
            result.append(-i)

        # If n is odd, add 0
        if n % 2 == 1:
            result.append(0)

        return result
