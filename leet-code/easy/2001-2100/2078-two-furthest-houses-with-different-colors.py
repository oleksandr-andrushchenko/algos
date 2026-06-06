# There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed
# integer array colors of length n, where colors[i] represents the color of the ith house.
#
# Return the maximum distance between two houses with different colors.
#
# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)

        left_max = 0
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                left_max = i
                break

        right_max = 0
        for i in range(n):
            if colors[i] != colors[-1]:
                right_max = n - 1 - i
                break

        return max(left_max, right_max)
