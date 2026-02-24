# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
#
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water,
# and there is exactly one island (i.e., one or more connected land cells).
#
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
# One cell is a square with side length 1.
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Start with 4 edges
                    perimeter += 4

                    # Subtract edges for each adjacent land cell
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2  # shared edge with top
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2  # shared edge with left

        return perimeter
