# Alice and Bob are playing a game where they take turns removing stones from a pile, with Alice going first.
#
# Alice starts by removing exactly 10 stones on her first turn.
# For each subsequent turn, each player removes exactly 1 fewer stone than the previous opponent.
# The player who cannot make a move loses the game.
#
# Given a positive integer n, return true if Alice wins the game and false otherwise.

class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice_turn = True

        while n >= stones:
            n -= stones
            stones -= 1
            alice_turn = not alice_turn

        return not alice_turn
