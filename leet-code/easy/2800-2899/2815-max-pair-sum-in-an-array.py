# You are given an integer array nums. You have to find the maximum sum of a pair of numbers from nums such that the
# largest digit in both numbers is equal.
#
# For example, 2373 is made up of three distinct digits: 2, 3, and 7, where 7 is the largest among them.
#
# Return the maximum sum or -1 if no such pair exists.

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        largest = {}
        answer = -1

        for num in nums:
            max_digit = max(str(num))

            if max_digit in largest:
                answer = max(answer, num + largest[max_digit])

            largest[max_digit] = max(largest.get(max_digit, 0), num)

        return answer
