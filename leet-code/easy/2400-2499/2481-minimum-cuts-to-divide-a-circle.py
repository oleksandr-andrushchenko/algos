# A valid cut in a circle can be:
#
# A cut that is represented by a straight line that touches two points on the edge of the circle and passes through its
# center, or
# A cut that is represented by a straight line that touches one point on the edge of the circle and its center.
# Some valid and invalid cuts are shown in the figures below.
#
#
# Given the integer n, return the minimum number of cuts needed to divide a circle into n equal slices.

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0

        # One full diameter creates two equal slices.
        # For even n, each cut can create two opposite slices.
        if n % 2 == 0:
            return n // 2

        # For odd n, every cut must go from the center to the edge.
        return n
