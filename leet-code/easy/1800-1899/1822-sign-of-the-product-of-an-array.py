# Implement a function signFunc(x) that returns:
#
# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.
# You are given an integer array nums. Let product be the product of all values in the array nums.
#
# Return signFunc(product).

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        sign = 1

        for num in nums:
            if num == 0:
                return 0

            if num < 0:
                sign *= -1

        return sign
