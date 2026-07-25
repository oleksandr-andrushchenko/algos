# You are given a positive integer n. Each digit of n has a sign according to the following rules:
#
# The most significant digit is assigned a positive sign.
# Each other digit has an opposite sign to its adjacent digits.
# Return the sum of all digits with their corresponding sign.

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0
        sign = 1

        for digit in str(n):
            answer += sign * int(digit)
            sign *= -1

        return answer
