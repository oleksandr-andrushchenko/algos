# You are given an integer array nums.
#
# The binary reflection of a positive integer is defined as the number obtained by reversing the order of its binary
# digits (ignoring any leading zeros) and interpreting the resulting binary number as a decimal.
#
# Sort the array in ascending order based on the binary reflection of each element. If two different numbers have the
# same binary reflection, the smaller original number should appear first.
#
# Return the resulting sorted array.

from typing import List


class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        return sorted(
            nums,
            key=lambda n: (int(bin(n)[:1:-1], 2), n)
        )
