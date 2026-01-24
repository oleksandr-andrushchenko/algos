# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in
# non-decreasing order.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n

        l, r = 0, n - 1
        pos = n - 1

        while l <= r:
            left_sq = nums[l] * nums[l]
            right_sq = nums[r] * nums[r]

            if left_sq > right_sq:
                res[pos] = left_sq
                l += 1
            else:
                res[pos] = right_sq
                r -= 1

            pos -= 1

        return res
