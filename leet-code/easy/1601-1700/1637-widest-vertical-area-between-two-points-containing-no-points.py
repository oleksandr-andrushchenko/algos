# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that
# no points are inside the area.
#
# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest
# vertical area is the one with the maximum width.
#
# Note that points on the edge of a vertical area are not considered included in the area.

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        xs = sorted(x for x, _ in points)

        max_gap = 0
        for i in range(1, len(xs)):
            max_gap = max(max_gap, xs[i] - xs[i - 1])

        return max_gap
