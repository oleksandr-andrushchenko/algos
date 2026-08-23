# You are given a binary string s that contains at least one '1'.
#
# You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can
# be created from this combination.
#
# Return a string representing the maximum odd binary number that can be created from the given combination.
#
# Note that the resulting string can have leading zeros.

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = len(s) - ones

        return '1' * (ones - 1) + '0' * zeros + '1'
