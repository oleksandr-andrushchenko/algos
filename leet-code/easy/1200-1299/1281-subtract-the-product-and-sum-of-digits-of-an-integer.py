# Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summ = 0

        for c in str(n):
            digit = int(c)
            product *= digit
            summ += digit

        return product - summ