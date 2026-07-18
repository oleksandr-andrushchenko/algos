# You are given a 0-indexed integer array nums of even length.
#
# As long as nums is not empty, you must repetitively:
#
# Find the minimum number in nums and remove it.
# Find the maximum number in nums and remove it.
# Calculate the average of the two removed numbers.
# The average of two numbers a and b is (a + b) / 2.
#
# For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.
# Return the number of distinct averages calculated using the above process.
#
# Note that when there is a tie for a minimum or maximum number, any can be removed.

from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = set()

        left = 0
        right = len(nums) - 1

        while left < right:
            # Store the sum instead of dividing by 2.
            averages.add(nums[left] + nums[right])
            left += 1
            right -= 1

        return len(averages)
