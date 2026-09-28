# You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square on an 8 x 8
# chessboard.
#
# Below is the chessboard for reference.
#
#
#
# Return true if these two squares have the same color and false otherwise.
#
# The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first
# (indicating its column), and the number second (indicating its row).

class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def color(coordinate: str) -> int:
            col = ord(coordinate[0]) - ord("a")
            row = int(coordinate[1]) - 1

            return (row + col) % 2

        return color(coordinate1) == color(coordinate2)
