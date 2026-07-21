# The value of an alphanumeric string can be defined as:
#
# The numeric representation of the string in base 10, if it comprises of digits only.
# The length of the string, otherwise.
# Given an array strs of alphanumeric strings, return the maximum value of any string in strs.

from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0

        for s in strs:
            if s.isdigit():
                ans = max(ans, int(s))
            else:
                ans = max(ans, len(s))

        return ans
