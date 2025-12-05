# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different
# size r x c keeping its original data.
#
# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns
# of the wanted reshaped matrix.
#
# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as
# they were.
#
# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise,
# output the original matrix.

class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        # Check if reshape is possible
        if m * n != r * c:
            return mat

        # Flatten
        flat = [num for row in mat for num in row]

        # Build new matrix
        reshaped = []
        idx = 0
        for _ in range(r):
            reshaped.append(flat[idx:idx + c])
            idx += c

        return reshaped
