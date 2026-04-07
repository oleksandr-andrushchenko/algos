# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that
# there are exactly x numbers in nums that are greater than or equal to x.
#
# Notice that x does not have to be an element in nums.
#
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is
# unique.

class Solution:
    def specialArray(self, nums: list[int]) -> int:
        n = len(nums)

        for x in range(n + 1):
            count = sum(1 for num in nums if num >= x)
            if count == x:
                return x

        return -1
