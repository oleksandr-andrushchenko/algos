# You are given a 0-indexed integer array nums and an integer k.
#
# Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their
# binary representation.
#
# The set bits in an integer are the 1's present when it is written in binary.
#
# For example, the binary representation of 21 is 10101, which has 3 set bits.

from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0

        for i, num in enumerate(nums):
            if i.bit_count() == k:
                result += num

        return result
