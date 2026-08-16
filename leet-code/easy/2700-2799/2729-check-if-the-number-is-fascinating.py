# You are given an integer n that consists of exactly 3 digits.
#
# We call the number n fascinating if, after the following modification, the resulting number contains all the digits
# from 1 to 9 exactly once and does not contain any 0's:
#
# Concatenate n with the numbers 2 * n and 3 * n.
# Return true if n is fascinating, or false otherwise.
#
# Concatenating two numbers means joining them together. For example, the concatenation of 121 and 371 is 121371.

class Solution:
    def isFascinating(self, n: int) -> bool:
        value = str(n) + str(2 * n) + str(3 * n)

        return len(value) == 9 and set(value) == set("123456789")
