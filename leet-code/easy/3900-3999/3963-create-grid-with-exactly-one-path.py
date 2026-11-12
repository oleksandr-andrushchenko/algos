# You are given two integers m and n, representing the number of rows and columns of a grid.
#
# Construct any m x n grid consisting only of the characters '.' and '#', where:
#
# '.' represents a free cell.
# '#' represents an obstacle cell.
# A valid path is a sequence of free cells that:
#
# Starts at the top-left cell (0, 0).
# Ends at the bottom-right cell (m - 1, n - 1).
# Moves only:
# Right, from (i, j) to (i, j + 1), or
# Down, from (i, j) to (i + 1, j).
# Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n] + [
            "#" * (n - 1) + "." for _ in range(m - 1)
        ]
