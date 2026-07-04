# You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some
# number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.
#
# A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another
# piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.
#
# Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if
# there is another piece blocking the path.
#
# Return the number of pawns the white rook is attacking.

class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        # Find the rook
        r = c = -1
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r, c = i, j
                    break
            if r != -1:
                break

        captures = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] == 'B':
                    break
                if board[nr][nc] == 'p':
                    captures += 1
                    break
                nr += dr
                nc += dc

        return captures
