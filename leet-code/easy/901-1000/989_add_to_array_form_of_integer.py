# The array-form of an integer num is an array representing its digits in left to right order.
#
# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        res = []
        i = len(num) - 1

        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]
                i -= 1

            res.append(k % 10)
            k //= 10

        return res[::-1]
