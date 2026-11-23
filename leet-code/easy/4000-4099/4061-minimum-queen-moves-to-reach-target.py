# There is an 8 x 8 empty chessboard with 1-indexed rows and columns.
#
# You are given an array source = [sr, sc] representing the starting position of a queen, and an array
# target = [tr, tc] representing the target position.
#
# In one move, the queen travels one or more squares along a single row, column, or diagonal, staying within the board.
#
# Return the minimum number of moves for the queen to land exactly on target.

class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if source == target:
            return 0

        sr, sc = source
        tr, tc = target

        if sr == tr or sc == tc or abs(sr - tr) == abs(sc - tc):
            return 1

        return 2
