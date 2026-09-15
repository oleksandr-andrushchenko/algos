# You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents the
# white color, and character 'B' represents the black color.
#
# Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the
# same color.
#
# Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.

from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for row in range(2):
            for col in range(2):
                cells = [
                    grid[row][col],
                    grid[row][col + 1],
                    grid[row + 1][col],
                    grid[row + 1][col + 1],
                ]

                if cells.count("B") >= 3 or cells.count("W") >= 3:
                    return True

        return False
