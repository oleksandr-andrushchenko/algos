# You are given integers n, m, and k.
#
# There are two logs of lengths n and m units, which need to be transported in three trucks where each truck can carry
# one log with length at most k units.
#
# You may cut the logs into smaller pieces, where the cost of cutting a log of length x into logs of length len1 and
# len2 is cost = len1 * len2 such that len1 + len2 = x.
#
# Return the minimum total cost to distribute the logs onto the trucks. If the logs don't need to be cut, the total
# cost is 0.


class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        if n <= k and m <= k:
            return 0

        x = max(n, m)
        return k * (x - k)
