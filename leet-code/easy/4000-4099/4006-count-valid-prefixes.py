# You are given a binary string s.
#
# A prefix of s is considered valid if its characters can be rearranged to form an alternating string.
#
# Return the number of valid prefixes of s.
#
# A string is considered alternating if no two adjacent characters are equal.

class Solution:
    def countValidPrefixes(self, s: str) -> int:
        balance = 0
        count = 0

        for char in s:
            balance += 1 if char == "1" else -1

            if abs(balance) <= 1:
                count += 1

        return count
