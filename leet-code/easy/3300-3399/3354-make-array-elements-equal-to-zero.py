# You are given an integer array nums.
#
# Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left
# or right.
#
# After that, you repeat the following process:
#
# If curr is out of the range [0, n - 1], this process ends.
# If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr
# if you are moving left.
# Else if nums[curr] > 0:
# Decrement nums[curr] by 1.
# Reverse your movement direction (left becomes right and vice versa).
# Take a step in your new direction.
# A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0
# by the end of the process.
#
# Return the number of possible valid selections.

from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        result = 0

        for num in nums:
            if num == 0:
                right_sum = total - left_sum

                if left_sum == right_sum:
                    result += 2
                elif abs(left_sum - right_sum) == 1:
                    result += 1

            left_sum += num

        return result
