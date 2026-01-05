# Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle
# that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        n = len(points)
        max_area = 0.0

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]

                    area = abs(
                        x1 * (y2 - y3) +
                        x2 * (y3 - y1) +
                        x3 * (y1 - y2)
                    ) / 2.0

                    max_area = max(max_area, area)

        return max_area
