# You are given an integer array cost of size n. You are currently at position n (at the end of the line) in a line of
# n + 1 people (numbered from 0 to n).
#
# You wish to move forward in the line, but each person in front of you charges a specific amount to swap places. The
# cost to swap with person i is given by cost[i].
#
# You are allowed to swap places with people as follows:
#
# If they are in front of you, you must pay them cost[i] to swap with them.
# If they are behind you, they can swap with you for free.
# Return an array answer of size n, where answer[i] is the minimum total cost to reach each position i in the line.


from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        result = []
        min_cost = float('inf')

        for c in cost:
            min_cost = min(min_cost, c)
            result.append(min_cost)

        return result
