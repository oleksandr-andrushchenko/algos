# Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and
# the number of ones in that row.
#
# In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be
# selected.
#
# Return an array containing the index of the row, and the number of ones in it.

from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = [0, 0]

        for i, row in enumerate(mat):
            ones = sum(row)

            if ones > answer[1]:
                answer = [i, ones]

        return answer
