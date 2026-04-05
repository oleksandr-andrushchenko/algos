# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that
# are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            total += mat[i][i]  # primary diagonal
            total += mat[i][n - 1 - i]  # secondary diagonal

        # If n is odd, subtract the middle element once (it was counted twice)
        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total
