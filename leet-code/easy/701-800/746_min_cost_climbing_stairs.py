# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you
# can either climb one or two steps.
#
# You can either start from the step with index 0, or the step with index 1.
#
# Return the minimum cost to reach the top of the floor.

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)

        prev2 = cost[0]  # dp[0]
        prev1 = cost[1]  # dp[1]

        for i in range(2, n):
            curr = cost[i] + min(prev1, prev2)
            prev2, prev1 = prev1, curr

        return min(prev1, prev2)
