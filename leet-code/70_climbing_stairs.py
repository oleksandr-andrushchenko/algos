# You are climbing a staircase.
# It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?

from functools import lru_cache


class Solution:
    @classmethod
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n):
        if n <= 2:
            return n
        f1, f2 = 1, 2
        for _ in range(3, n + 1):
            f1, f2 = f2, f1 + f2
        return f2
