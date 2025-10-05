# Given an integer rowIndex, return the row Indexth (0-indexed) row of the Pascal's triangle.

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [a + b for a, b in zip(row, row[1:])] + [1]
        return row
