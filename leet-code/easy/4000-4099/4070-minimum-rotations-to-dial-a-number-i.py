# You are given a string s of length 10 consisting of digits.
#
# The dial contains the digits 0 through 9 in order and is circular, so 0 and 9 are adjacent. The pointer initially
# points to 0.
#
# To dial each digit of s in order, rotate the pointer until it points to that digit. Each rotation moves the pointer to
# an adjacent digit, and you may rotate in either direction. Dialing a digit that the pointer already points to requires no rotations.
#
# Return the minimum total number of rotations needed to dial every digit of s.

class Solution:
    def minRotations(self, s: str) -> int:
        current = 0
        total = 0

        for char in s:
            digit = int(char)
            distance = abs(digit - current)
            total += min(distance, 10 - distance)
            current = digit

        return total
