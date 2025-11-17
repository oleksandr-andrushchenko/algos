# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
#
# Given the integer n, return the number of complete rows of the staircase you will build.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            if coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right
