# You are given an array nums, where each number in the array appears either once or twice.
#
# Return the bitwise XOR of all the numbers that appear twice in the array, or 0 if no number appears twice.

from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        seen = set()
        result = 0

        for num in nums:
            if num in seen:
                result ^= num
            else:
                seen.add(num)

        return result
