# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of
# the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting
# from the pixel image[sr][sc].
#
# To perform a flood fill:
#
# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel,
# either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches
# the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        original = image[sr][sc]

        # If the color is the same, nothing to change
        if original == color:
            return image

        def dfs(r: int, c: int) -> None:
            if (
                    r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    image[r][c] != original
            ):
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image
