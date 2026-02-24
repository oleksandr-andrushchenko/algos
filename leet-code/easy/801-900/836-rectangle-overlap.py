# An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its
# bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to
# the X-axis, and its left and right edges are parallel to the Y-axis.
#
# Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at
# the corner or edges do not overlap.
#
# Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2

        return not (
                x2 <= x3 or  # rec1 is left of rec2
                x4 <= x1 or  # rec2 is left of rec1
                y2 <= y3 or  # rec1 is below rec2
                y4 <= y1  # rec2 is below rec1
        )
