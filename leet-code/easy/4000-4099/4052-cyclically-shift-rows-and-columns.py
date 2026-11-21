# You are given an integer n, a 2D integer array grid of size n x n, and two integer arrays rowShift and colShift, each
# of length n, where:
#
# rowShift[i] represents the number of positions to cyclically shift the ith row of grid to the left.
# colShift[j] represents the number of positions to cyclically shift the jth column of grid upward.
# First, cyclically shift each row according to rowShift, then cyclically shift each column of the resulting grid
# according to colShift.
#
# Return the resulting grid after performing all the shifts.
#
# A cyclic left shift of a row by k positions moves the element at column j to column (j - k + n) % n. All other rows
# remain unchanged.
#
# A cyclic upward shift of a column by k positions moves the element at row i to row (i - k + n) % n. All other columns
# remain unchanged.

class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        result = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                new_col = (j - rowShift[i]) % n
                new_row = (i - colShift[new_col]) % n
                result[new_row][new_col] = grid[i][j]

        return result
