# You are given an integer n representing the number of players in a game and a 2D array pick where pick[i] = [xi, yi]
# represents that the player xi picked a ball of color yi.
#
# Player i wins the game if they pick strictly more than i balls of the same color. In other words,
#
# Player 0 wins if they pick any ball.
# Player 1 wins if they pick at least two balls of the same color.
# ...
# Player i wins if they pick at least i + 1 balls of the same color.
# Return the number of players who win the game.
#
# Note that multiple players can win the game.

from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        counts = [{} for _ in range(n)]

        for player, color in pick:
            counts[player][color] = counts[player].get(color, 0) + 1

        result = 0

        for player in range(n):
            if any(count > player for count in counts[player].values()):
                result += 1

        return result
