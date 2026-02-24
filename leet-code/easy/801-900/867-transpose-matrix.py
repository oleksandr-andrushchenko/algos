# Given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        transposed = [[0] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                transposed[j][i] = matrix[i][j]

        return transposed
