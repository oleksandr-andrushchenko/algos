# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
# A divisor of an integer x is an integer that can divide x evenly.
#
# Given an integer n, return true if n is a perfect number, otherwise return false.

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False

        total = 1  # 1 is always a divisor

        # Check divisors up to sqrt(num)
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                other = num // i
                if other != i:  # avoid adding square root twice
                    total += other
            i += 1

        return total == num
