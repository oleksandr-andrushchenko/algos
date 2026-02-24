# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are
# a boomerang.
#
# A boomerang is a set of three points that are all distinct and not in a straight line.

class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        # Check that all points are distinct
        if len({tuple(p) for p in points}) < 3:
            return False

        # Extract points
        (x1, y1), (x2, y2), (x3, y3) = points

        # Check for collinearity using slope comparison
        # Slope between p1-p2: (y2 - y1) / (x2 - x1)
        # Slope between p1-p3: (y3 - y1) / (x3 - x1)
        # Avoid division by zero by cross-multiplying:
        return (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1)
