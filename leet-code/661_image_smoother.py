# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding down the average
# of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother).
# If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average
# of the four cells in the red smoother).
#
#
# Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother
# on each cell of it.

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        m, n = len(img), len(img[0])
        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                total = 0
                count = 0

                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < m and 0 <= nj < n:
                            total += img[ni][nj]
                            count += 1

                result[i][j] = total // count

        return result
