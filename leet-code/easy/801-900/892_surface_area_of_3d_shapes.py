# You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower
# of v cubes placed on top of cell (i, j).
#
# After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several
# irregular 3D shapes.
#
# Return the total surface area of the resulting shapes.
#
# Note: The bottom face of each shape counts toward its surface area.

class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]
                if h > 0:
                    area += 2 + 4 * h

                if i + 1 < n:
                    area -= 2 * min(h, grid[i + 1][j])

                if j + 1 < n:
                    area -= 2 * min(h, grid[i][j + 1])

        return area
