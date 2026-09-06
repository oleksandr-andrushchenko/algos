# You are given a 2D 0-indexed integer array dimensions.
#
# For all indices i, 0 <= i < dimensions.length, dimensions[i][0] represents the length and dimensions[i][1] represents
# the width of the rectangle i.
#
# Return the area of the rectangle having the longest diagonal. If there are multiple rectangles with the longest
# diagonal, return the area of the rectangle having the maximum area.

from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0

        for length, width in dimensions:
            diagonal = length * length + width * width
            area = length * width

            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = area
            elif diagonal == max_diagonal:
                max_area = max(max_area, area)

        return max_area
