# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
#
# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli].
# return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw".
# If there are still movements to play return "Pending".
#
# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        rows = [0] * 3
        cols = [0] * 3
        diag = 0
        anti_diag = 0

        for i, (r, c) in enumerate(moves):
            player = 1 if i % 2 == 0 else -1  # A = 1, B = -1

            rows[r] += player
            cols[c] += player

            if r == c:
                diag += player
            if r + c == 2:
                anti_diag += player

            # Check win condition
            if (abs(rows[r]) == 3 or
                    abs(cols[c]) == 3 or
                    abs(diag) == 3 or
                    abs(anti_diag) == 3):
                return "A" if player == 1 else "B"

        # If all 9 moves played and no winner
        if len(moves) == 9:
            return "Draw"

        return "Pending"
