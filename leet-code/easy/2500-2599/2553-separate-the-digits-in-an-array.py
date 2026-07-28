# Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums
# after separating them in the same order they appear in nums.
#
# To separate the digits of an integer is to get all the digits it has in the same order.
#
# For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for num in nums:
            for digit in str(num):
                answer.append(int(digit))

        return answer
