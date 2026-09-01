# You are given two positive integers n and limit.
#
# Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0

        for first in range(min(n, limit) + 1):
            remaining = n - first

            low = max(0, remaining - limit)
            high = min(limit, remaining)

            if low <= high:
                ans += high - low + 1

        return ans
