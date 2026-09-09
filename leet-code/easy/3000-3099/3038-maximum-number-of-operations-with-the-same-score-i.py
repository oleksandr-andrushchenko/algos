# You are given an array of integers nums. Consider the following operation:
#
# Delete the first two elements nums and define the score of the operation as the sum of these two elements.
# You can perform this operation until nums contains fewer than two elements. Additionally, the same score must be
# achieved in all operations.
#
# Return the maximum number of operations you can perform.

from typing import List


class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        score = nums[0] + nums[1]
        ans = 0

        for i in range(0, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] != score:
                break

            ans += 1

        return ans
