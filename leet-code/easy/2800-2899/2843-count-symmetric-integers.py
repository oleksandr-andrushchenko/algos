# You are given two positive integers low and high.
#
# An integer x consisting of 2 * n digits is symmetric if the sum of the first n digits of x is equal to the sum of the
# last n digits of x. Numbers with an odd number of digits are never symmetric.
#
# Return the number of symmetric integers in the range [low, high].

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            s = str(num)

            if len(s) % 2 != 0:
                continue

            mid = len(s) // 2

            if sum(map(int, s[:mid])) == sum(map(int, s[mid:])):
                count += 1

        return count
