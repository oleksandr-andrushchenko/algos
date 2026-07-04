# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of
# negative numbers in grid.

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row, col = 0, n - 1
        count = 0

        while row < m and col >= 0:
            if grid[row][col] < 0:
                count += m - row
                col -= 1
            else:
                row += 1

        return count
