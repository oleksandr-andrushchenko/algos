# Given a positive integer num, return true if num is a perfect square or false otherwise.
#
# A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
#
# You must not use any built-in library function, such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
