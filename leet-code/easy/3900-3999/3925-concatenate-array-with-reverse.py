# You are given an integer array nums of length n.
#
# Construct a new array ans of length 2 * n such that the first n elements are the same as nums, and the next n elements
# are the elements of nums in reverse order.
#
# Formally, for 0 <= i <= n - 1:
#
# ans[i] = nums[i]
# ans[i + n] = nums[n - i - 1]
# Return an integer array ans.

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        return nums + nums[::-1]
