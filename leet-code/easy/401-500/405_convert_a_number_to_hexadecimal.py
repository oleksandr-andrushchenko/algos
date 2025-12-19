# Given a 32-bit integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.
#
# All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.
#
# Note: You are not allowed to use any built-in library method to directly solve this problem.

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        # handle negative numbers using two's complement for 32-bit
        num &= 0xFFFFFFFF

        hex_chars = "0123456789abcdef"
        result = ""

        while num > 0:
            digit = num & 0xF  # take last 4 bits
            result = hex_chars[digit] + result
            num >>= 4  # shift right by 4 bits

        return result
