# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.
#
# In one shift operation:
#
# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.

class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                old_index = i * n + j
                new_index = (old_index + k) % total

                new_i = new_index // n
                new_j = new_index % n

                result[new_i][new_j] = grid[i][j]

        return result
