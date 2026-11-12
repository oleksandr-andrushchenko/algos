# You are given a positive integer n.
#
# Let digitSum be the sum of the digits of n, and let squareSum be the sum of the squares of the digits of n.
#
# An integer is called good if squareSum - digitSum >= 50.
#
# Return true if n is good. Otherwise, return false.

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        difference = 0

        while n:
            n, digit = divmod(n, 10)
            difference += digit * digit - digit

        return difference >= 50
