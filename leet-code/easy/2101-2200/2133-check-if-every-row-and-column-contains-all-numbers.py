# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.

from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        required = set(range(1, n + 1))

        # Check rows
        for row in matrix:
            if set(row) != required:
                return False

        # Check columns
        for col in range(n):
            if {matrix[row][col] for row in range(n)} != required:
                return False

        return True
