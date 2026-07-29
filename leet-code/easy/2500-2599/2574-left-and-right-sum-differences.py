# You are given a 0-indexed integer array nums of size n.
#
# Define two arrays leftSum and rightSum where:
#
# leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element,
# leftSum[i] = 0.
# rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element,
# rightSum[i] = 0.
# Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        answer = []

        for num in nums:
            right_sum -= num
            answer.append(abs(left_sum - right_sum))
            left_sum += num

        return answer
