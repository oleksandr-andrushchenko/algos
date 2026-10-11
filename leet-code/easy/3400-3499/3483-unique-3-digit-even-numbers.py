# You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even
# numbers that can be formed using these digits.
#
# Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.


from itertools import permutations
from typing import List


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                numbers.add(a * 100 + b * 10 + c)

        return len(numbers)
