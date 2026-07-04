# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating
# mat in 90-degree increments, or false otherwise.

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True

            mat = self.rotate(mat)

        return False

    def rotate(self, mat: list[list[int]]) -> list[list[int]]:
        n = len(mat)
        rotated = [[0] * n for _ in range(n)]

        for row in range(n):
            for col in range(n):
                rotated[col][n - 1 - row] = mat[row][col]

        return rotated
