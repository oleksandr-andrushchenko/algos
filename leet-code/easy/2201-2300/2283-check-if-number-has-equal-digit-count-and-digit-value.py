# You are given a 0-indexed string num of length n consisting of digits.
#
# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return
# false.

from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        counts = Counter(num)

        for i, digit in enumerate(num):
            if counts[str(i)] != int(digit):
                return False

        return True
