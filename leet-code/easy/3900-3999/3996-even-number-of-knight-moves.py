# You are given two integer arrays start and target, where each array is of the form [x, y] representing a cell on a
# standard 8 x 8 chessboard.
#
# Return true if a knight can move from start to target in an even number of moves. Otherwise, return false.
#
# Note: A valid knight move consists of moving two squares in one direction and one square perpendicular to it. The
# figure below illustrates all eight possible moves from a cell.

class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        return sum(start) % 2 == sum(target) % 2
