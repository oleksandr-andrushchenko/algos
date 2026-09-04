# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears
# exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers
# a and b.
#
# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeated = -1

        for row in grid:
            for num in row:
                if num in seen:
                    repeated = num
                seen.add(num)

        for num in range(1, n * n + 1):
            if num not in seen:
                return [repeated, num]

        return []
