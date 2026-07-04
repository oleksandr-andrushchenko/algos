# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
#
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the
# day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
#
# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7  # full weeks
        r = n % 7  # remaining days

        # sum of full weeks
        # 28 + 35 + 42 + ... (k terms)
        full_weeks = k * 28 + 7 * (k * (k - 1) // 2)

        # sum of remaining days
        # starts from (k + 1)
        remaining = r * (2 * (k + 1) + (r - 1)) // 2

        return full_weeks + remaining
