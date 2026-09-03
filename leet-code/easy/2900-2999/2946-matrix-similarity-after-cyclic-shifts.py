# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.
#
# The following process happens k times:
#
# Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
#
#
# Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
#
#
# Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k %= n

        for i, row in enumerate(mat):
            if i % 2 == 0:
                shifted = row[k:] + row[:k]
            else:
                shifted = row[-k:] + row[:-k] if k else row

            if shifted != row:
                return False

        return True
