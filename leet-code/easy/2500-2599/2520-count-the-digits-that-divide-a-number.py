# Given an integer num, return the number of digits in num that divide num.
#
# An integer val divides nums if nums % val == 0.

class Solution:
    def countDigits(self, num: int) -> int:
        answer = 0

        for digit in str(num):
            if num % int(digit) == 0:
                answer += 1

        return answer
