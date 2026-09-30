# In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number
# was supposed to appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making
# the list longer than usual.
#
# As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two
# numbers (in any order), so peace can return to Digitville.

from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        result = []

        for num in nums:
            if num in seen:
                result.append(num)
            else:
                seen.add(num)

        return result
