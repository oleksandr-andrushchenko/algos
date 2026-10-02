# Given an integer array hours representing times in hours, return an integer denoting the number of pairs i, j where
# \i < j and hours[i] + hours[j] forms a complete day.
#
# A complete day is defined as a time duration that is an exact multiple of 24 hours.
#
# For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.

from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        counts = [0] * 24
        result = 0

        for hour in hours:
            remainder = hour % 24
            complement = (-remainder) % 24

            result += counts[complement]
            counts[remainder] += 1

        return result
