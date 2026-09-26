# You are given a n x n 2D array grid containing distinct elements in the range [0, n2 - 1].
#
# Implement the NeighborSum class:
#
# NeighborSum(int [][]grid) initializes the object.
# int adjacentSum(int value) returns the sum of elements which are adjacent neighbors of value, that is either to the
# top, left, right, or bottom of value in grid.
# int diagonalSum(int value) returns the sum of elements which are diagonal neighbors of value, that is either to the
# top-left, top-right, bottom-left, or bottom-right of value in grid.

from typing import List


class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.n = len(grid)
        self.positions = {}

        for row in range(self.n):
            for col in range(self.n):
                self.positions[grid[row][col]] = (row, col)

    def adjacentSum(self, value: int) -> int:
        row, col = self.positions[value]
        result = 0

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + dr, col + dc

            if 0 <= r < self.n and 0 <= c < self.n:
                result += self.grid[r][c]

        return result

    def diagonalSum(self, value: int) -> int:
        row, col = self.positions[value]
        result = 0

        for dr, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            r, c = row + dr, col + dc

            if 0 <= r < self.n and 0 <= c < self.n:
                result += self.grid[r][c]

        return result

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
