# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
# The digits are ordered from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        i = l - 1

        while i > -1 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        if i == -1:
            return [1] + digits

        digits[i] += 1
        return digits
