# You are given an integer array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        dx = x2 - x1
        dy = y2 - y1

        for x, y in coordinates[2:]:
            if (y - y1) * dx != (x - x1) * dy:
                return False

        return True
