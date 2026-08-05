# You are given a 0-indexed m x n integer matrix grid. The width of a column is the maximum length of its integers.
#
# For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
# Return an integer array ans of size n where ans[i] is the width of the ith column.
#
# The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.

from typing import List


class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        answer = [0] * cols

        for col in range(cols):
            for row in range(rows):
                answer[col] = max(answer[col], len(str(grid[row][col])))

        return answer
