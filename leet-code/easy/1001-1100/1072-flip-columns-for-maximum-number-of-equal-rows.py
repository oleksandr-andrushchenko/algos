# You are given an m x n binary matrix matrix.
#
# You can choose any number of columns in the matrix and flip every cell in that column
# (i.e., Change the value of the cell from 0 to 1 or vice versa).
#
# Return the maximum number of rows that have all values equal after some number of flips.

from collections import Counter


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        counter = Counter()

        for row in matrix:
            # Normalize row
            if row[0] == 1:
                normalized = tuple(1 - bit for bit in row)
            else:
                normalized = tuple(row)

            counter[normalized] += 1

        return max(counter.values())
