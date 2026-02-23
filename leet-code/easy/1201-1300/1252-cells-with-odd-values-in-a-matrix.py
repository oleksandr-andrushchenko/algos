# There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each
# indices[i] = [ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.
#
# For each location indices[i], do both of the following:
#
# Increment all the cells on row ri.
# Increment all the cells on column ci.
# Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the increment to all
# locations in indices.

class Solution:
    def oddCells(self, m: int, n: int, indices: list[list[int]]) -> int:
        row_count = [0] * m
        col_count = [0] * n

        for r, c in indices:
            row_count[r] += 1
            col_count[c] += 1

        odd_rows = sum(r % 2 for r in row_count)
        odd_cols = sum(c % 2 for c in col_count)

        return odd_rows * (n - odd_cols) + (m - odd_rows) * odd_cols
