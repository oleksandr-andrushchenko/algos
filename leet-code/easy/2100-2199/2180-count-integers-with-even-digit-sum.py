# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are
# even.
#
# The digit sum of a positive integer is the sum of all its digits.

class Solution:
    def countEven(self, num: int) -> int:
        count = 0

        for i in range(1, num + 1):
            if sum(map(int, str(i))) % 2 == 0:
                count += 1

        return count
