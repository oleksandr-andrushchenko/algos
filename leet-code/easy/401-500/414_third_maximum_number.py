# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None

        for num in nums:
            # Skip duplicates
            if num == first or num == second or num == third:
                continue

            if first is None or num > first:
                first, second, third = num, first, second
            elif second is None or num > second:
                second, third = num, second
            elif third is None or num > third:
                third = num

        return third if third is not None else first
