# Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to matrix,
# then replace each element with the value -1 with the maximum element in its respective column.
#
# Return the matrix answer.

from typing import List


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])

        for col in range(cols):
            max_value = max(matrix[row][col] for row in range(rows))

            for row in range(rows):
                if matrix[row][col] == -1:
                    matrix[row][col] = max_value

        return matrix
