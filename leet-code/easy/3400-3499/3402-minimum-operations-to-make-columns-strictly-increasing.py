# You are given a m x n matrix grid consisting of non-negative integers.
#
# In one operation, you can increment the value of any grid[i][j] by 1.
#
# Return the minimum number of operations needed to make all columns of grid strictly increasing.

from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0

        for col in range(cols):
            for row in range(1, rows):
                if grid[row][col] <= grid[row - 1][col]:
                    target = grid[row - 1][col] + 1
                    result += target - grid[row][col]
                    grid[row][col] = target

        return result
