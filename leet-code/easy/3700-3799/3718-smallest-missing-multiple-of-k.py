# Given an integer array nums and an integer k, return the smallest positive multiple of k that is missing from nums.
#
# A multiple of k is any positive integer divisible by k.


from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        seen = set(nums)
        multiple = k

        while multiple in seen:
            multiple += k

        return multiple
