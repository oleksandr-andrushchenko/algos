# You are given a 2D matrix grid of size m x n. You need to check if each cell grid[i][j] is:
#
# Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
# Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
# Return true if all the cells satisfy these conditions, otherwise, return false.

from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if i + 1 < rows and grid[i][j] != grid[i + 1][j]:
                    return False

                if j + 1 < cols and grid[i][j] == grid[i][j + 1]:
                    return False

        return True