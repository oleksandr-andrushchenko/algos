# Given an m x n binary matrix mat, return the number of special positions in mat.
#
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and
# columns are 0-indexed).

class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        row_count = [0] * m
        col_count = [0] * n

        # Count ones in rows and columns
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1

        # Count special positions
        result = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    result += 1

        return result
