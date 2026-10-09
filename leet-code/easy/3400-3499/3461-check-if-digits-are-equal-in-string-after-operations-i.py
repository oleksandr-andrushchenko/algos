# You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly
# two digits:
#
# For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two
# digits modulo 10.
# Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
# Return true if the final two digits in s are the same; otherwise, return false.


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(c) for c in s]

        while len(digits) > 2:
            digits = [
                (digits[i] + digits[i + 1]) % 10
                for i in range(len(digits) - 1)
            ]

        return digits[0] == digits[1]
