# Given a positive integer num represented as a string, return the integer num without trailing zeros as a string.

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")
