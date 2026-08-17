# You are given a 0-indexed integer array nums. A pair of indices i, j where 0 <= i < j < nums.length is called beautiful
# if the first digit of nums[i] and the last digit of nums[j] are coprime.
#
# Return the total number of beautiful pairs in nums.
#
# Two integers x and y are coprime if there is no integer greater than 1 that divides both of them. In other words, x
# and y are coprime if gcd(x, y) == 1, where gcd(x, y) is the greatest common divisor of x and y.

from math import gcd
from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        first_digits = [0] * 10
        answer = 0

        for num in nums:
            last_digit = num % 10

            for digit in range(1, 10):
                if gcd(digit, last_digit) == 1:
                    answer += first_digits[digit]

            first_digit = int(str(num)[0])
            first_digits[first_digit] += 1

        return answer
