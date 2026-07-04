# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s, split it into some number of substrings such that:
#
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        result = 0

        for char in s:
            if char == 'L':
                balance += 1
            else:  # char == 'R'
                balance -= 1

            if balance == 0:
                result += 1

        return result
