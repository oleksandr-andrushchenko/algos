# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])

        # Minimum value in each row
        row_mins = [min(row) for row in matrix]

        # Maximum value in each column
        col_maxs = [max(matrix[i][j] for i in range(m)) for j in range(n)]

        # Lucky numbers are those that are row_min and col_max
        result = [matrix[i][j]
                  for i in range(m)
                  for j in range(n)
                  if matrix[i][j] == row_mins[i] and matrix[i][j] == col_maxs[j]]

        return result
