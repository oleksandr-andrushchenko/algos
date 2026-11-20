# You are given a string s consisting of lowercase English letters.
#
# Construct a binary string by replacing each character in s with the 8-bit binary representation of its ASCII value,
# including leading zeros, while preserving the original order of the characters.
#
# Return true if the resulting binary string is a palindrome. Otherwise, return false.

class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary = "".join(f"{ord(char):08b}" for char in s)
        return binary == binary[::-1]
