# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
#
# An alphanumeric string is a string consisting of lowercase English letters and digits.

class Solution:
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1

        for ch in s:
            if ch.isdigit():
                num = int(ch)

                if num > first:
                    second = first
                    first = num
                elif first > num > second:
                    second = num

        return second
